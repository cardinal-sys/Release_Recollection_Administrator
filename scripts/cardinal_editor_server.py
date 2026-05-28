#!/usr/bin/env python3
"""Cardinal Editor static server + GitHub sync API.

Serves the editor/ directory at http://localhost:3001.
Provides POST /api/github-sync to commit keymap changes to GitHub.

◆ 同期フロー
  1. フロントから ZMK Studio keymap JSON を送信
  2. サーバーが JSON → .keymap ソース変換（binding レベル、layer ファイル個別更新）
  3. GitHub Contents API（PUT）で各ファイルを更新し、コミット

◆ 認証
  リクエスト JSON に { "pat": "<token>", "keymap": {...} } を含める。
  PAT はメモリ内のみに保持し、ログにも出力しない。
"""
import base64
import http.server
import json
import os
import re
import socketserver
import urllib.error
import urllib.request

PORT = 3001
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDITOR_DIR = os.path.join(ROOT, "editor")

GITHUB_REPO = "cardinal-sys/Release_Recollection_Administrator"
GITHUB_API  = "https://api.github.com"

# ──────────────────────────────────────────────
# keymap 変換ヘルパー
# ──────────────────────────────────────────────

# ZMK HID Usage → keycode 文字列
# page=7 (Keyboard/Keypad), page=12 (Consumer)
_KBD_MAP = {
    # Letters
    4: "A", 5: "B", 6: "C", 7: "D", 8: "E", 9: "F", 10: "G",
    11: "H", 12: "I", 13: "J", 14: "K", 15: "L", 16: "M",
    17: "N", 18: "O", 19: "P", 20: "Q", 21: "R", 22: "S",
    23: "T", 24: "U", 25: "V", 26: "W", 27: "X", 28: "Y", 29: "Z",
    # Digits
    30: "NUMBER_1", 31: "NUMBER_2", 32: "NUMBER_3", 33: "NUMBER_4",
    34: "NUMBER_5", 35: "NUMBER_6", 36: "NUMBER_7", 37: "NUMBER_8",
    38: "NUMBER_9", 39: "NUMBER_0",
    # Special
    40: "ENTER", 41: "ESC", 42: "BACKSPACE", 43: "TAB", 44: "SPACE",
    45: "MINUS", 46: "EQUAL", 47: "LEFT_BRACKET", 48: "RIGHT_BRACKET",
    49: "BACKSLASH", 51: "SEMICOLON", 52: "SINGLE_QUOTE", 53: "GRAVE",
    54: "COMMA", 55: "PERIOD", 56: "SLASH",
    57: "CAPS",
    # F keys
    58: "F1", 59: "F2", 60: "F3", 61: "F4", 62: "F5", 63: "F6",
    64: "F7", 65: "F8", 66: "F9", 67: "F10", 68: "F11", 69: "F12",
    70: "PRINTSCREEN", 73: "INSERT", 74: "HOME", 75: "PAGE_UP",
    76: "DELETE", 77: "END", 78: "PAGE_DOWN",
    79: "RIGHT_ARROW", 80: "LEFT_ARROW", 81: "DOWN_ARROW", 82: "UP_ARROW",
    # F13-F24
    104: "F13", 105: "F14", 106: "F15", 107: "F16", 108: "F17",
    109: "F18", 110: "F19", 111: "F20", 112: "F21", 113: "F22",
    114: "F23", 115: "F24",
    # Modifiers
    224: "LEFT_CONTROL", 225: "LEFT_SHIFT", 226: "LEFT_ALT", 227: "LEFT_GUI",
    228: "RIGHT_CONTROL", 229: "RIGHT_SHIFT", 230: "RIGHT_ALT", 231: "RIGHT_GUI",
}

_CONSUMER_MAP = {
    0xCD: "C_PLAY_PAUSE",
    0xE2: "C_MUTE",
    0xE9: "C_VOLUME_UP",
    0xEA: "C_VOLUME_DOWN",
    0xB5: "C_NEXT",
    0xB6: "C_PREVIOUS",
}

_MOD_NAMES = {
    0x01: "LCTRL", 0x02: "LSHFT", 0x04: "LALT", 0x08: "LGUI",
    0x10: "RCTRL", 0x20: "RSHFT", 0x40: "RALT", 0x80: "RGUI",
}

_MOUSE_MAP = {1: "MB1", 2: "MB2", 4: "MB3", 8: "MB4", 16: "MB5"}


def _hid_to_kc(usage: int) -> str:
    """HID usage value → ZMK keycode string."""
    implicit_mods = (usage >> 24) & 0xFF
    page          = (usage >> 16) & 0xFF
    key_id        = usage & 0xFFFF

    if page == 7:
        kc = _KBD_MAP.get(key_id, f"0x{key_id:04X}")
    elif page == 12:
        kc = _CONSUMER_MAP.get(key_id, f"0x{key_id:04X}")
    else:
        return f"/* unknown usage 0x{usage:08X} */"

    if implicit_mods:
        mods = [n for m, n in _MOD_NAMES.items() if implicit_mods & m]
        chain = "(".join(f"L{m}(" for m in mods)
        close = ")" * len(mods)
        return f"&kp {chain}{kc}{close}"

    return kc


def _binding_to_zmk(b: dict, behaviors: dict) -> str:
    """ZMK Studio binding dict → ZMK binding string."""
    bid   = b.get("behaviorId", 0)
    p1    = b.get("param1", 0) or 0
    p2    = b.get("param2", 0) or 0
    bname = behaviors.get(bid, {}).get("displayName", f"behavior#{bid}")

    if bname in ("Transparent",):
        return "&trans"
    if bname in ("None",):
        return "&none"
    if bname in ("Bootloader",):
        return "&bootloader"
    if bname in ("Reset",):
        return "&sys_reset"
    if bname in ("Studio Unlock",):
        return "&studio_unlock"

    if bname == "Key Press":
        page   = (p1 >> 16) & 0xFF
        key_id = p1 & 0xFFFF
        implicit = (p1 >> 24) & 0xFF
        if page == 12:
            kc = _CONSUMER_MAP.get(key_id, f"0x{key_id:04X}")
            if implicit:
                mods = [n for m, n in _MOD_NAMES.items() if implicit & m]
                chain = "".join(f"L{m}(" for m in mods)
                close = ")" * len(mods)
                return f"&kp {chain}{kc}{close}"
            return f"&kp {kc}"
        kc = _KBD_MAP.get(key_id, f"0x{key_id:04X}")
        if implicit:
            mods = [n for m, n in _MOD_NAMES.items() if implicit & m]
            chain = "".join(f"L{m}(" for m in mods)
            close = ")" * len(mods)
            return f"&kp {chain}{kc}{close}"
        return f"&kp {kc}"

    if bname == "Mod-Tap":
        # p1 = mod mask, p2 = HID (tap)
        mods = "_".join(n for m, n in _MOD_NAMES.items() if p1 & m) or f"0x{p1:02X}"
        kc = _KBD_MAP.get(p2 & 0xFFFF, f"0x{p2:04X}")
        return f"&mt {mods} {kc}"

    if bname == "Layer-Tap":
        kc = _KBD_MAP.get(p2 & 0xFFFF, f"0x{p2:04X}")
        return f"&lt {p1} {kc}"

    if bname == "Momentary Layer":
        return f"&mo {p1}"

    if bname == "Toggle Layer":
        return f"&tog {p1}"

    if bname == "To Layer":
        return f"&to {p1}"

    if bname == "Sticky Key":
        page   = (p1 >> 16) & 0xFF
        key_id = p1 & 0xFFFF
        if page == 7:
            kc = _KBD_MAP.get(key_id, f"0x{key_id:04X}")
        else:
            kc = f"0x{key_id:04X}"
        return f"&sk {kc}"

    if bname == "Sticky Layer":
        return f"&sl {p1}"

    if bname == "Mouse Key Press":
        btn = _MOUSE_MAP.get(p1, f"MB{p1}")
        return f"&mkp {btn}"

    if bname == "Key Repeat":
        kc = _KBD_MAP.get(p1 & 0xFFFF, f"0x{p1:04X}")
        return f"&key_repeat {kc}"

    if bname == "Key Toggle":
        kc = _KBD_MAP.get(p1 & 0xFFFF, f"0x{p1:04X}")
        return f"&kt {kc}"

    if bname == "Grave/Escape":
        kc = _KBD_MAP.get(p1 & 0xFFFF, f"0x{p1:04X}")
        return f"&gresc {kc}"

    if bname == "Output Selection":
        labels = {0: "OUT_AUTO", 1: "OUT_USB", 2: "OUT_BLE"}
        return f"&out {labels.get(p1, str(p1))}"

    if bname == "External Power":
        labels = {0: "EP_OFF", 1: "EP_ON", 2: "EP_TOG"}
        return f"&ext_power {labels.get(p1, str(p1))}"

    # Fallback: unknown behavior → comment
    return f"/* {bname}({p1},{p2}) */"


# ──────────────────────────────────────────────
# 既存 .dtsi からレイヤー変数名・sensor-bindings を保持するパーサ
# ──────────────────────────────────────────────

_LAYER_FILES = [
    ("00_default.dtsi",    "default_layer"),
    ("01_function.dtsi",   "FUNCTION"),
    ("02_sign.dtsi",       "SIGN"),
    ("03_num.dtsi",        "NUM"),
    ("04_mouse.dtsi",      "MOUSE"),
    ("05_scroll.dtsi",     "SCROLL"),
    ("06_bluetooth.dtsi",  "Bluetooth"),
    ("07_gesture_e.dtsi",  "GESTURE_E"),
    ("08_gesture_r.dtsi",  "GESTURE_R"),
    ("09_gesture_s.dtsi",  "GESTURE_S"),
    ("10_gesture_b.dtsi",  "GESTURE_B"),
    ("11_gesture_t.dtsi",  "GESTURE_T"),
    ("12_gesture_a.dtsi",  "GESTURE_A"),
    ("13_gesture_d.dtsi",  "GESTURE_D"),
    ("14_gesture_w.dtsi",  "GESTURE_W"),
    ("15_snipe.dtsi",      "SNIPE"),
    ("16_num_smart.dtsi",  "NUM_SMART"),
]


def _read_file_meta(fname: str) -> dict:
    """既存 dtsi ファイルのヘッダコメントと sensor-bindings を抽出する。"""
    path = os.path.join(ROOT, "config", "keymap", "layers", fname)
    try:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return {"header": "", "sensor": None}

    header_m = re.match(r"(/\*.*?\*/)\n", src, re.DOTALL)
    header = header_m.group(0) if header_m else ""

    sensor_m = re.search(r"(sensor-bindings\s*=\s*<[^>]+>;)", src)
    sensor = sensor_m.group(1) if sensor_m else None

    return {"header": header, "sensor": sensor}


def keymap_json_to_dtsi_files(km_json: dict) -> dict:
    """
    ZMK Studio getKeymap レスポンス JSON と behavior map を受け取り、
    各レイヤーの .dtsi 文字列を生成して返す。

    km_json = {
        "layers": [ { "id": int, "name": str, "bindings": [...] } ],
        "behaviors": { id(int): { "displayName": str } }
    }

    Returns: { "config/keymap/layers/XX_xxx.dtsi": "<new content>", ... }
    """
    layers    = km_json.get("layers", [])
    behaviors = {int(k): v for k, v in km_json.get("behaviors", {}).items()}

    result = {}

    for layer_idx, (fname, var_name) in enumerate(_LAYER_FILES):
        if layer_idx >= len(layers):
            break

        layer = layers[layer_idx]
        bindings = layer.get("bindings", [])

        meta = _read_file_meta(fname)

        bind_strs = [_binding_to_zmk(b, behaviors) for b in bindings]
        bindings_line = "    " + "  ".join(bind_strs)

        lines = []
        if meta["header"]:
            lines.append(meta["header"].rstrip())
        else:
            lines.append(
                f"/* ============================================================\n"
                f" * layers/{fname} — [ Synthesis {layer_idx:02d} ] {var_name}\n"
                f" * ============================================================ */"
            )

        lines.append("")
        lines.append(f"{var_name} {{")
        lines.append("    bindings = <")
        lines.append(bindings_line)
        lines.append("    >;")
        if meta["sensor"]:
            lines.append("")
            lines.append(f"    {meta['sensor']}")
        lines.append("};")
        lines.append("")

        path_key = f"config/keymap/layers/{fname}"
        result[path_key] = "\n".join(lines)

    return result


# ──────────────────────────────────────────────
# GitHub API ヘルパー
# ──────────────────────────────────────────────

def _github_request(method: str, url: str, pat: str, data: dict | None = None):
    """GitHub REST API リクエストを発行する。"""
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, method=method, data=body)
    req.add_header("Authorization", f"token {pat}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode()), resp.status
    except urllib.error.HTTPError as e:
        body_txt = e.read().decode(errors="replace")
        return {"error": e.reason, "detail": body_txt, "code": e.code}, e.code


def _get_file_sha(pat: str, path: str, branch: str = "main") -> str | None:
    """ファイルの現在 SHA を取得する（PUT に必要）。"""
    url = f"{GITHUB_API}/repos/{GITHUB_REPO}/contents/{path}?ref={branch}"
    data, status = _github_request("GET", url, pat)
    if status == 200:
        return data.get("sha")
    return None


def _put_file(pat: str, path: str, content: str, message: str,
              branch: str = "main", sha: str | None = None) -> tuple[bool, str]:
    """ファイルを作成 / 更新する。"""
    url = f"{GITHUB_API}/repos/{GITHUB_REPO}/contents/{path}"
    encoded = base64.b64encode(content.encode("utf-8")).decode()
    payload: dict = {
        "message": message,
        "content": encoded,
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha
    data, status = _github_request("PUT", url, pat, payload)
    if status in (200, 201):
        return True, data.get("commit", {}).get("sha", "")
    return False, data.get("detail", str(data))


# ──────────────────────────────────────────────
# HTTP Handler
# ──────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=EDITOR_DIR, **kwargs)

    def log_message(self, fmt, *args):
        # PAT が混入しないよう path のみ出力
        print(f"[cardinal-editor] {self.command} {self.path}", flush=True)

    def do_OPTIONS(self):
        """CORS preflight."""
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_POST(self):
        if self.path == "/api/github-sync":
            self._handle_github_sync()
        else:
            self.send_response(404)
            self.end_headers()

    def _handle_github_sync(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as e:
            self._json_resp(400, {"ok": False, "error": f"JSON parse error: {e}"})
            return

        pat      = payload.get("pat", "").strip()
        km_json  = payload.get("keymap")
        branch   = payload.get("branch", "main")
        commit_msg = payload.get("commitMessage", "").strip() or \
            "feat(live-sync): 〈Memory Inscription〉— Live Sync Conduit から keymap を同期"

        if not pat:
            self._json_resp(400, {"ok": False, "error": "PAT が未設定です"})
            return
        if not km_json:
            self._json_resp(400, {"ok": False, "error": "keymap データがありません"})
            return

        print(f"[github-sync] branch={branch} layers={len(km_json.get('layers',[]))}", flush=True)

        # keymap JSON → dtsi ファイル群に変換
        try:
            dtsi_files = keymap_json_to_dtsi_files(km_json)
        except Exception as e:
            self._json_resp(500, {"ok": False, "error": f"変換エラー: {e}"})
            return

        results = []
        any_error = False

        for fpath, content in dtsi_files.items():
            sha = _get_file_sha(pat, fpath, branch)
            ok, info = _put_file(pat, fpath, content, commit_msg, branch, sha)
            results.append({"file": fpath, "ok": ok, "info": info if not ok else "updated"})
            if not ok:
                any_error = True
                print(f"[github-sync] ERROR {fpath}: {info}", flush=True)
            else:
                print(f"[github-sync] OK    {fpath}", flush=True)

        status = 500 if any_error else 200
        self._json_resp(status, {
            "ok": not any_error,
            "results": results,
            "branch": branch,
        })

    def _json_resp(self, code: int, data: dict):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)


class ReuseAddrTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with ReuseAddrTCPServer(("localhost", PORT), Handler) as httpd:
        print(f"[cardinal-editor] Serving {EDITOR_DIR} at http://localhost:{PORT}", flush=True)
        print(f"[cardinal-editor] GitHub Sync API: POST http://localhost:{PORT}/api/github-sync", flush=True)
        httpd.serve_forever()
