◆══════════════════════════════════════◆

# << ADMINISTRATOR >>

*最高司祭の権能 — Release Recollection 50-Key Edition*

◆══════════════════════════════════════◆

> **[ SYSTEM ANNOUNCEMENT ]**
> 公理は記憶を統べる。50の権限が世界を編纂する。
> 神器〈Night_Sky_Sword〉と〈Blue_Rose_Sword〉が叛逆の双剣となり、
> Cardinal の継承者として記憶解放術を顕現する。
> ── System Call, Enhance Armament. Administrator Awakening.

══════════════════════════════════════════════

## ◆ KEYMAP DISPLAY ── キーマップ図

> [ CARDINAL ] Push のたびに自動更新されます（`.github/workflows/draw-keymap.yml`）

![keymap](keymap.svg)

══════════════════════════════════════════════

## ◆ CARDINAL EDITOR ── 記憶書換術式

*管理者権限を以て神器の記憶を直接書き換える Web 術式。ブラウザ上で `keymap.yaml` のキーを視覚編集し、`config/` 以下の DTS / YAML / overlay / conf を全域編纂し、〈Sealing〉により GitHub へ一括封印（コミット）する。*

> **[ CARDINAL ]** 〈Cardinal Editor〉は静的サイトとして `editor/` 配下に構築されている。GitHub API + Tree API を直接叩いて複数ファイルを 1 コミットで送信する設計。

### ◆ 〈Live Sync Conduit〉── 直接接続術式（Phase 2 / PoC）

`editor/live.html` で **公式 ZMK Studio と同じ Web Bluetooth プロトコル**による直接接続を実現する PoC。`@zmkfirmware/zmk-studio-ts-client@0.0.18` を **esm.sh 経由でビルド不要に組み込み**、Service UUID `00000000-0196-6107-c967-c5cfb1c2482a` の GATT サービスへ接続する。

| 段階 | 状態 |
|---|---|
| Step 1: ZMK Studio 有効化（`CONFIG_ZMK_STUDIO=y`） | ✅ |
| Step 2: PoC（Web Bluetooth 接続 + Transport 確立） | ✅ |
| Step 3: RPC キーマップ取得・書換 + Visual Editor 同期 | ✅ |

> **[ SYSTEM ]** Live Sync Conduit を使うには Night_Sky_Sword (central) に ZMK Studio 有効化版ファームウェアが書き込まれている必要がある。Chrome / Edge など Web Bluetooth API 対応ブラウザ必須。

### ◆ 起動方法 ── Invocation

#### 〈オンライン〉GitHub Pages（推奨）

`.github/workflows/deploy-editor.yml` により main ブランチの `editor/` が
自動的に GitHub Pages へデプロイされる。HTTPS なので Web Bluetooth API が
最も安定する。

| 入口 | URL |
|---|---|
| Cardinal Editor (git 編纂) | `https://cardinal-sys.github.io/Release_Recollection_Administrator/index.html` |
| Live Sync Conduit (実機接続) | `https://cardinal-sys.github.io/Release_Recollection_Administrator/live.html` |

> **[ SYSTEM ]** 初回利用時は GitHub の Settings → Pages で Source を
> "GitHub Actions" に設定する必要がある。

#### 〈オフライン〉launchd 常駐（macOS）

ローカルマシンに Cardinal Editor サーバを常駐させる：

```bash
# 常駐化
bash scripts/install_launchd.sh

# 解除
bash scripts/uninstall_launchd.sh
```

常駐後、`http://localhost:3001` でいつでも利用可能。
ログは `~/Library/Logs/cardinal-editor/server.log`。

#### 〈ワンショット〉手動起動

```bash
python3 scripts/cardinal_editor_server.py
# または
python3 -m http.server 3001 --directory editor
```

#### 〈ネイティブ〉Tauri デスクトップ版（実験段階）

Web Bluetooth は macOS の HID 接続済みデバイスを再選択できない仕様の制約があり、
Live Sync の BLE 接続が安定しない。Tauri デスクトップ版は **OS ネイティブ Bluetooth API** を
直接叩くため、HID 接続中でも BLE 接続が可能（公式 ZMK Studio Tauri 版と同等）。

##### 必要環境
- Rust toolchain（`rustup` 経由）
- Node.js 20+ + npm
- macOS の場合: Xcode Command Line Tools

##### セットアップ
```bash
# Rust 未インストールなら
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Tauri CLI
npm install
```

##### 起動
```bash
# 開発モード（Cardinal Editor サーバ自動起動）
npm run tauri:dev

# リリースビルド（.dmg / .app を生成）
npm run tauri:build
```

ビルド成果物は `src-tauri/target/release/bundle/` 配下に生成される。

##### リリース配布
タグ `v*` を push すると `.github/workflows/tauri-build.yml` が走り、
macOS (Universal) / Windows / Linux 向け **.dmg / .msi / .deb / .AppImage** が
自動ビルドされて GitHub Releases にドラフト公開される。

```bash
# 例: v0.1.0 をリリース
git tag v0.1.0
git push origin v0.1.0
```

> **[ SYSTEM ]** Phase A は editor/ embed のみ、Phase B で Rust BLE transport
> 実装、Phase C で UI 上の Web/Tauri バッジ表示、Phase D で CI による
> マルチプラットフォームビルドを完備。Web Bluetooth の制約を完全突破。

### ◆ 認証関門 ── Authentication Gate

GitHub Personal Access Token（`repo` スコープ必須）をブラウザに入力。トークンは localStorage にのみ保存され、GitHub API の Bearer 認証に使用される。

### ◆ 編纂対象 ── Editable Modules

| 領域 | ファイル |
|---|---|
| キーマップ描画 | `keymap.yaml` `keymap_drawer.yaml` |
| 神器エントリ | `config/Administrator.keymap` |
| コンボ術式 | `config/keymap/10_combos.dtsi` |
| マクロ術式 | `config/keymap/20_macros.dtsi` |
| Enhance Armament | `config/keymap/30_*` `31_*` `35_*` |
| 剣技（ジェスチャー） | `config/keymap/40_*` 〜 `47_*` |
| 階層（レイヤー） | `config/keymap/layers/*.dtsi` |
| Shield 設定 | `config/boards/shields/Administrator/*` |
| west.yml | `config/west.yml` |

### ◆ 編纂モード ── Edit Modes

- **Code Editor** — CodeMirror による DTS / YAML 構文ハイライト + 括弧マッチング + Active Line Highlight
- **Visual Editor**（`keymap.yaml` 限定）— `config/Administrator.json` のレイアウト座標から **左右分割の物理キーボード配置を再現**。親指列の回転（`r:`）も `transform: rotate()` で忠実に表現。レイヤー切替タブ + キーのクリック編纂で `t:` `h:` を直接書換
- **Quick Pick**（神器選択候補）— レイヤー / 修飾キー / 文字 / 数字 / F1-F24 / 矢印 / 特殊キー / 記号 / ZMK behavior / **剣技 (Sword Skills)** / 使用中の値 の 11 カテゴリから値を選択可能。剣技カテゴリには 8 神器 × 4 方向 = 32 種の `&gE_*` 〜 `&gW_*` 全 mod-morph behavior が含まれる。Tap/Hold いずれにも適用ターゲットを切替可能。`<datalist>` でオートコンプリートも併設
- **Modifier Toggles**（修飾キー独立選択）— `Sft` / `Ctl` / `Alt` / `Gui` をチップ式チェックボックスで個別トグル。選択状態は対象フィールド（Tap / Hold）の値に **`Sft+Ctl+TAB` 形式で自動結合**される。既存値の修飾キープレフィックスもパースして UI に反映、双方向同期

### ◆ 封印術式 ── Sealing Protocol

複数ファイル変更を 1 コミットで送信する Tree API 連鎖：

1. ブランチ ref → base commit → base tree を取得
2. 変更ファイルごとに Blob 生成
3. 新規 Tree を作成（base_tree からの差分）
4. 新規 Commit を作成（parent = base commit）
5. ブランチ ref を新 Commit へ更新

> **[ SYSTEM ]** 〈Sealing〉は確認ダイアログを経由する。誤封印を防ぐカーディナル安全装置。

══════════════════════════════════════════════

## ◆ SYNTHESIS REGISTRY ── レイヤー構成

*カーディナルシステムにより展開されたシンセシス一覧。アクティブなシンセシスは STATUS CRYSTAL が示す。*

| SYNTHESIS | NAME | DESCRIPTION |
|---|---|---|
| [ Synthesis 00 ] | default | 通常入力 |
| [ Synthesis 01 ] | FUNCTION | ファンクションキー・カーソル |
| [ Synthesis 02 ] | SIGN | 記号入力（括弧・引用符・各種記号）|
| [ Synthesis 03 ] | NUM | 右手テンキー / 左手は編集ショートカット（⌘A/X/C/V/Z/Y, ^⌥V, ⌘↑3, ⌘↑4, END）|
| [ Synthesis 04 ] | MOUSE | マウス操作 |
| [ Synthesis 05 ] | SCROLL | スクロール |
| [ Synthesis 06 ] | Bluetooth | BT接続切替・bootloader |
| [ Synthesis 07 ] | GESTURE_E | ジェスチャー（E キー長押し）|
| [ Synthesis 08 ] | GESTURE_R | ジェスチャー（R キー長押し）|
| [ Synthesis 09 ] | GESTURE_S | ジェスチャー（S キー長押し）|
| [ Synthesis 10 ] | GESTURE_B | ジェスチャー（B キー長押し）|
| [ Synthesis 11 ] | GESTURE_T | ジェスチャー（T キー長押し）|
| [ Synthesis 12 ] | GESTURE_A | ジェスチャー（A キー長押し）|
| [ Synthesis 13 ] | GESTURE_D | ジェスチャー（D キー長押し）|
| [ Synthesis 14 ] | GESTURE_W | ジェスチャー（W キー長押し）|
| [ Synthesis 15 ] | SNIPE | スマートスネイプ（Tab ホールド or L2+L3 同時ホールドで起動。デフォルトと同一バインド、CPI 自動低減。クリック・キー入力で自動解除。**K ホールド中はトラックボールがスクロールホイールに変換される**）|
| [ Synthesis 16 ] | NUM_SMART | スマート数字入力（数字キーで自動維持） |

══════════════════════════════════════════════

## ◆ ENHANCE ARMAMENT ── 武装完全支配術

*神器に宿る記憶を辿り、武装の挙動と形態を支配する下位術式。〈Release Recollection〉が神器の真名そのものを解き放つ最上位術式であるのに対し、〈Enhance Armament〉はその挙動を細部まで支配する基盤術式群を司る。*

> **[ CARDINAL ]** 武装制御系 behavior の責務分割。`config/keymap/` 以下に術式階位ごと分離されている。

### ◆ 術式階位 ── Arts Hierarchy

| 階位 | 術式名 | 役割 |
|---|---|---|
| 上位 | **Release Recollection**（記憶解放術）| 神器の真名 ─ keymap entry point。全シンセシスを統括する最上位術式 |
| 下位 | **Enhance Armament**（武装完全支配術）| 武装の挙動制御 ─ 基礎behavior／階層behavior／拡張behavior の三系統で構成 |

### ◆ 術式構成ファイル ── Sacred Modules

| ファイル | 階層 | 担う術式 |
|---|---|---|
| `config/keymap/30_enhance_armament_base.dtsi` | 基礎術式 | hold-tap / sensor-rotate / sticky-key / tri-state（神器の根源挙動） |
| `config/keymap/31_enhance_armament_layers.dtsi` | 階層術式 | レイヤー制御behavior / auto-layer（神器の階層遷移） |
| `config/keymap/35_enhance_armament.dtsi` | 拡張術式 | 拡張behaviorの依代。将来の昇華に備えた予約領域 |

> **[ SYSTEM ]** 拡張術式ファイル `35_enhance_armament.dtsi` は現時点で空。新規導入する武器制御術式はこの依代に記される。

══════════════════════════════════════════════

## ◆ KEYSTROKE MECHANICS ── 操作感チューニング

*〈Enhance Armament〉基礎術式の調律。フラクトライトの応答特性を制御する hold-tap behavior。誤入力を防ぎながら意図した長押しを正確に認識する。*

### Hold-Tap Behavior Matrix

*各 behavior の設定は、双剣運用時の誤入力抑制と素早い反応のバランスを取っている。*

| Behavior | flavor | tapping-term-ms | quick-tap-ms | require-prior-idle-ms | hold-trigger-key-positions | 役割 |
|---|---|---|---|---|---|---|
| `gesture_mo_kp` | tap-preferred | 210 | 150 | 450 | — | ジェスチャーレイヤー（E,R,S,D,W等の長押し） |

──────────────────────────────────────────────

## ◆ SWORD SKILLS ── ジェスチャーマッピング表

*剣技は身体の記憶に刻まれている。対応キーを**長押ししながらセンサーを動かした瞬間**、技が解放される。*
*上下左右 4 方向を認識。Shift 同時押しで上位技へと昇華する。*

──────────────────────────────────────────────

### ◆ SWORD SKILL : SHARP NAIL  [ KEY : E ] ── GESTURE_E（E キー長押し）― 編集剣技

*素早い連続斬撃。コピー・カット・ペーストを一息に刻み込む。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Cmd+C` コピー | `Cmd+X` カット |
| ↓ 下 | `Cmd+V` ペースト | `Cmd+Shift+V` フォーマットなしペースト |
| ← 左 | `Cmd+Z` アンドゥ | `Cmd+P` |
| → 右 | `Cmd+Shift+Z` リドゥ | `Cmd+Return` |

──────────────────────────────────────────────

### ◆ SWORD SKILL : VORPAL STRIKE  [ KEY : R ] ── GESTURE_R（R キー長押し）― 選択剣技

*渾身の一撃でテキストを貫く。精密な範囲指定を一刀両断する。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Cmd+A` 全選択 | `Cmd+Shift+↑` |
| ↓ 下 | `Cmd+X` カット | `Cmd+Shift+↓` |
| ← 左 | `Alt+Shift+←` 単語選択（左） | `Cmd+Shift+←` 行頭まで選択 |
| → 右 | `Alt+Shift+→` 単語選択（右） | `Cmd+Shift+→` 行末まで選択 |

──────────────────────────────────────────────

### ◆ SWORD SKILL : THE ECLIPSE  [ KEY : S ] ── GESTURE_S（S キー長押し）― 捕捉剣技

*全てを覆い封じる最終奥義。画面そのものを闇に刻み込む。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Cmd+Shift+3` 全画面スクショ（ファイル保存） | `Ctrl+Cmd+Shift+3` 全画面（クリップボード） |
| ↓ 下 | `Escape` | `Escape` |
| ← 左 | `Cmd+Shift+4` 範囲選択スクショ | `Ctrl+Cmd+Shift+4` 範囲選択（クリップボード） |
| → 右 | `Cmd+Shift+5` スクショメニュー | `Cmd+Shift+5` |

──────────────────────────────────────────────

### ◆ SWORD SKILL : HOWLING OCTAVE  [ KEY : B ] ── GESTURE_B（B キー長押し）― 音響剣技

*8連の咆哮が空間を震わせる。輝度と音量を意のままに操る。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | 輝度上げる | `F13` |
| ↓ 下 | 輝度下げる | ミュート |
| ← 左 | 音量下げる | `F19` |
| → 右 | 音量上げる | `F18` |

──────────────────────────────────────────────

### ◆ SWORD SKILL : SONIC LEAP  [ KEY : T ] ── GESTURE_T（T キー長押し）― 航路剣技

*音速で次の場所へ跳躍する。タブという扉を瞬時に開閉する。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Cmd+T` 新規タブ | `Cmd+R` リロード |
| ↓ 下 | `Cmd+W` タブを閉じる | `Cmd+F` 検索 |
| ← 左 | `Ctrl+Shift+Tab` 前のタブ | `Cmd+-` ズームアウト |
| → 右 | `Ctrl+Tab` 次のタブ | `Cmd++` ズームイン |

──────────────────────────────────────────────

### ◆ SWORD SKILL : VERTICAL SQUARE  [ KEY : A ] ── GESTURE_A（A キー長押し）― 探索剣技

*四方を刻む連続剣技。アプリの格子を縦横に切り裂き、目標へ飛ぶ。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Ctrl+B` | `Ctrl+Alt+Cmd+1` |
| ↓ 下 | `Cmd+Space` Spotlight | `Ctrl+Alt+Cmd+4` |
| ← 左 | `Cmd+Shift+Tab` アプリ切替（前） | `Ctrl+Alt+Cmd+3` |
| → 右 | `Cmd+Tab` アプリ切替（次） | `Ctrl+Alt+Cmd+2` |

──────────────────────────────────────────────

### ◆ SWORD SKILL : STARBURST STREAM  [ KEY : D ] ── GESTURE_D（D キー長押し）― 空間剣技

*16連の星屑が全方位を薙ぎ払う。Mission Control で全シンセシスを一望する。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `Ctrl+↑` Mission Control | `F12` |
| ↓ 下 | `Cmd+H` ウィンドウを隠す | `Ctrl+↓` |
| ← 左 | `F14` | `F11` |
| → 右 | `F15` | `F20` |

──────────────────────────────────────────────

### ◆ SWORD SKILL : HORIZONTAL  [ KEY : W ] ── GESTURE_W（W キー長押し）― 踏破剣技

*水平に薙ぐ一閃。左右に刻まれた履歴の軌跡を自在に辿る。*

| 方向 | 通常 | Shift 同時押し |
|---|---|---|
| ↑ 上 | `F3` ウィンドウを最大化　| `F17` |
| ↓ 下 | `Cmd+M` ウィンドウを最小化 | `F11` |
| ← 左 | `Cmd+[` ブラウザ戻る | `Cmd+Q` アプリ終了 |
| → 右 | `Cmd+]` ブラウザ進む | `Cmd+W` タブ/ウィンドウを閉じる |

══════════════════════════════════════════════

## ◆ MOVEMENT PARAMETERS ── トラックボール → キー変換（アロープロファイル）

*特定のシンセシスでは、トラックボールの動きがキー入力へと変換される。剣技とは独立した力で、**動かし続ける限り連続入力**される。*

### ◆ PRIMARY FORMATION ── 通常プロファイル（arrows-profiles）

| SYNTHESIS | 上 | 下 | 左 | 右 | one_shot | 備考 |
|---|---|---|---|---|---|---|
| 2 SIGN | 選択↑ | 選択↓ | 選択← | 選択→ | なし | 自動リピートなし |
| 3 NUM | `↑` | `↓` | `←` | `→` | なし | 加速あり |
| 6 Bluetooth | `強制終了(Cmd+Opt+Esc)` | `画面ロック(Ctrl+Cmd+Q)` | `LANG2(英数)` | `LANG1(かな)` | あり | 斜め無効・余り有効 |

### ◆ ALT FORMATION ── Shift 同時押し or arrows_alt 起動時（arrows-alt-profiles）

| SYNTHESIS | 上 | 下 | 左 | 右 | one_shot |
|---|---|---|---|---|---|
| 15 SNIPE | `SCROLL_UP` | `SCROLL_DOWN` | `SCROLL_LEFT` | `SCROLL_RIGHT` | なし |
| 2 SIGN | `Cmd+A` | `Cmd+V` | `Cmd+X` | `Cmd+C` | あり |
| 3 NUM | `Undo` | `Redo` | `BS` | `Del` | あり |
| 6 Bluetooth | 再生/停止(`C_PP`) | 停止(`C_STOP`) | 前のトラック(`C_PREV`) | 次のトラック(`C_NEXT`) | なし |

> **[ SYSTEM ]** L15 はキーバインドではなく `&ht_arrows_alt 15 K`（K ホールド）で起動。ドライバ拡張コード `2000-2003` が `input_report_rel(REL_WHEEL/REL_HWHEEL)` を直接発行するためホスト側はマウスホイールとして認識する。

> **[ SYSTEM ]** **one_shot** — 有効時、センサーの動きに対してキーが 1 度だけ送出される。
> 押しっぱなし状態にはならない。連続入力が不要な操作に適用される。

### ◆ ACCELERATION SYSTEM ── 加速設定（Synthesis 03）

- 閾値を超えると最大 1/4 速度まで加速
- 初回入力から 250ms 後に連続入力開始、100ms 間隔でリピート

══════════════════════════════════════════════

## ◆ STATUS CRYSTAL REGISTRY ── LED カラー（シンセシスインジケーター）

*アクティブなシンセシスに応じてクリスタルの発光色が変化する。現在位置をフラクトライトに知らせるインジケーター。*

| SYNTHESIS | COLOR |
|---|---|
| 0 default | 0 |
| 1 FUNCTION | 1 |
| 2 SIGN | 2 |
| 3 NUM | 3 |
| 4 MOUSE | 4 |
| 5 SCROLL | 5 |
| 6 Bluetooth | 6 |
| 7 GESTURE_E | 3 |
| 8 GESTURE_R | 4 |
| 9 GESTURE_S | 5 |
| 10 GESTURE_B | 0 |
| 11 GESTURE_T | 6 |
| 12 GESTURE_A | 7 |
| 13 GESTURE_D | 1 |
| 14 GESTURE_W | 2 |
| 15 SNIPE | 7 |
| 16 NUM_SMART | 3 |

══════════════════════════════════════════════

## ◆ EQUIPPED MODULES ── 依存モジュール

*このシステムを支える仲間たち。一つでも欠ければ、剣技は発動しない。*

| MODULE | REPOSITORY | DESCRIPTION |
|---|---|---|
| zmk | zmkfirmware/zmk | ZMK 本体 |
| zmk-pmw3610-driver | cardinal-sys/zmk-pmw3610-driver | PMW3610 トラックボールドライバー |
| zmk-listeners | ssbb/zmk-listeners | レイヤーリスナー |
| zmk-mouse-gesture | cardinal-sys/zmk-mouse-gesture | マウスジェスチャー認識 |
| zmk-scroll-snap | kot149/zmk-scroll-snap | スクロール軸スナップ（X/Y軸整列） |
| zmk-rgbled-widget | caksoylar/zmk-rgbled-widget | RGB LED インジケーター |
| zmk-pointing-acceleration-alpha | nuovotaka/zmk-pointing-acceleration-alpha | ポインタ加速度 |
| zmk-behavior-insomnia | badjeff/zmk-behavior-insomnia | BLE 接続中スリープ防止 |
| zmk-tri-state | urob/zmk-tri-state | アプリ切替スワッパー |
| zmk-auto-layer | urob/zmk-auto-layer | Smart Num（数字入力で自動レイヤー維持） |
| zmk-helpers | urob/zmk-helpers | キーマップ記述ヘルパーマクロ |

══════════════════════════════════════════════

## ◆ CHARACTER PARAMETERS ── 設定値サマリー

*フラクトライトの稼働を支える各種パラメータ。数値一つが安定と崩壊を分ける。*

### NERVE LINK STABILITY ── BLE・接続安定性

*STL とホストを繋ぐ生命線。接続が切れれば、フラクトライトは消滅する。*

| 設定 | 値 | 対象 | 効果 |
|---|---|---|---|
| Experimental Conn | R側(Night_Sky_Sword)のみ有効、L側無効 | R側（Central） | Central側でホスト向けBLE接続安定化のため有効化 |
| NFCT_PINS_AS_GPIOS | 有効 | R・L両側 | NFC無線とBLEの干渉防止（安定版2つともあり） |
| BT_GAP_AUTO_UPDATE_CONN_PARAMS | 有効 | R・L両側 | 接続後に自動パラメータ再交渉（kabutokoma準拠） |
| BT_CONN_PARAM_UPDATE_TIMEOUT | 1000ms | R・L両側 | 接続から1秒後にパラメータ更新要求 |
| BT_PERIPHERAL_PREF_TIMEOUT | 1000 (10秒) | R・L両側 | ホスト向け接続タイムアウト |
| TX Power | +8dBm | R・L両側 | 最大送信出力 |
| Split BLE Latency | 0 | R側（Central） | デフォルト 30 から 0 へ変更（Left 側キー入力の遅延パケット許容をゼロに） |
| Split BLE Timeout | 1000 | R・L両側 | スプリット接続タイムアウト（両側共通） |
| BT Max Conn | 6 | R・L両側 | 5プロファイル + 1スプリット接続（ZMK upstream の split central 既定値） |
| BT Max Paired | 6 | R・L両側 | `ZMK_BLE_PROFILE_COUNT = BT_MAX_PAIRED - PERIPHERALS = 6 - 1 = 5` で profile 0..4 全 5 枠を有効化 |
| BT_PERIPHERAL_PREF_MIN_INT | 6 (7.5ms) | R・L両側 | 接続インターバル下限 (Win/Android 最速側で 7.5ms 交渉) |
| BT_PERIPHERAL_PREF_MAX_INT | 12 (15ms) | R・L両側 | 接続インターバル上限 (Apple HID 互換上限。`MIN_INT=6` との範囲指定で macOS/iPadOS/iOS から最低 15ms を引き出す。L側もR側と同期) |
| Insomnia pingInterval | 3秒 | R・L両側 | keepaliveを高頻度化（L側にも追加） |

### MOTION SENSOR CONFIG ── トラックボールセンサー（Night_Sky_Sword.conf）

*センサーの挙動を制御するパラメータ。省電力モードへの移行速度を調整する。*

| 設定 | 値 | 効果 |
|---|---|---|
| PMW3610 REST移行時間 | 3000ms | RUN モード維持を延長し、短時間アイドル復帰の遅延を抑制 |
| PMW3610 REST1 サンプル間隔 | 10ms | REST 中のサンプリング間隔を半減し、復帰時の応答を改善 |
| PMW3610 ポーリングレート | 125Hz (POLLING_RATE_125) | 起動遅延を削除しポーリングレート固定モードに変更 |
| PMW3610 force-awake | 有効 | スリープ移行を抑制し、起動遅延ゼロを維持 |
| PMW3610 4ms モード | **無効**（削除済み） | BLE 7.5ms インターバルとのミスマッチによるポインタジャンプを防止 |
| PMW3610 CPI | 2200 | 通常カーソル CPI（`pointer_accel.sensor-dpi` も同値）。SNIPE 中はドライバが自動低減 |
| PMW3610 cpi-layers | `<4 3200>` | L4 MOUSE アクティブ時はセンサー CPI を 3200 に動的切替（〈Resolution Shift〉) |
| arrows-alt L15 tick | 80ms | K ホールドスクロールの精密度。値が大きいほど 1 ノッチが大きい動きを要求 |
| L5 SCROLL スケーラー | `1/1`（1x = 等速） | `zip_xy_to_scroll_mapper` 後段に `zip_snipe_scroll_scaler 1 1` を噛ませる現状は等速。`<1 2>` に変更すれば半速精密化に再昇華可能 |

### THREAD STACK ── スレッドスタック（クラッシュ対策）

*システムの安定を支える根幹。スタックが尽きればフラクトライトは瞬く間に崩壊する。*

| 設定 | 値 | 対象 | 備考 |
|---|---|---|---|
| EC11スレッド | 4096 bytes | Blue_Rose_Sword | |

══════════════════════════════════════════════

## ◆ INITIALIZATION PROTOCOL ── ビルド

*STL 起動。カーディナルシステムが世界を再生成する。*

> **[ CARDINAL ]** GitHub Actions により自動ビルド（`.github/workflows/build.yml`）。
> Push を契機に自動実行される。Artifacts から `.uf2` ファイルをダウンロードし、デバイスへ書き込むことで起動が完了する。

══════════════════════════════════════════════

## ◆ SYSTEM LOG ── 更新履歴

*カーディナルシステムの変更軌跡。刻まれた決定と解放された力の記録。*

| DATE | ENTRY |
|---|---|
| 2026-05-27 | 〈Native Embodiment Dissolution · Administrator Sync〉— 42キー Cardinal 側 [PR #20](https://github.com/cardinal-sys/Release_Recollection_Cardinal/pull/20) で先行解体された〈Native Embodiment〉Tauri デスクトップ版を 50キー〈Administrator〉側でも完全解体する儀式。 Cardinal は 2026-05-26 に解体済みだったが、Administrator 側は echo されておらず Tauri 残骸が居座っていた (twin symmetry audit で発覚)。 消去対象: `src-tauri/` 全体 (Cargo / Rust crate / Tauri 2.x config / icons / capabilities / src — 計 13 ファイル) / `package.json` (`cardinal-editor-tauri` Tauri CLI deps) / `.github/workflows/tauri-build.yml` (macOS Universal / Windows / Linux 自動ビルド CI 169 行) / `editor/live.js` の〈Tauri Native Bridge〉(`isTauri` / `tauriInvoke` / `tauriListen` / `showDevicePicker` / `connectBleTauri` 計 114 行 — Admin 固有の `Night_Sky_Sword` 風 name 優先ロジックも含む) + `handleConnectBle` の Tauri 分岐 + init 内 runtime バッジ更新 / `editor/app.js` の `isTauri()` / `tauri-badge` 表示ロジック / `editor/index.html` の `[ Native Embodiment Active ]` バッジ span / `editor/live.html` の `runtime-badge` (web/tauri 二系統) + BLE Device Picker Modal / `editor/style.css` の `.tauri-badge` 全消去 / `.gitignore` の Tauri / Rust / Node セクション。 Live Sync は **Web Bluetooth (Chrome/Edge) + Web Serial (USB-CDC ACM)** の二経路へ再収束、macOS で HID 接続中の Administrator を Web Bluetooth から再選択できない既知制約は表面化するが Cardinal と同じ回避策 (①OS Bluetooth で一時切断 → Web Bluetooth、②USB + Web Serial) で編纂可能。 〈Native Embodiment〉に関する歴史記録 (2026-05-05 PoC / 2026-05-10 Phase A / 2026-05-14 Conduit Re-Forging / Eternal Wait Sealing 等) は本 SYSTEM LOG にそのまま温存し術式の遍歴を証跡として残す。 これにより 42キー Cardinal と 50キー Administrator の `editor/` ツリーは Tauri 残骸ゼロの対称構成へ収束。 `feature/native-embodiment-dissolution-sync` ブランチで PR 化、GHA build 通過後に main マージ予定。 |
| 2026-05-27 | 〈Bilateral BLE Trinity · Administrator Sync〉— 42キー Cardinal 側で 2026-05-26〜27 に連続投入された BLE 三連改修 ([PR #21](https://github.com/cardinal-sys/Release_Recollection_Cardinal/pull/21) 〈Apple HID Interval Compat〉/ [PR #22](https://github.com/cardinal-sys/Release_Recollection_Cardinal/pull/22) 〈Phantom Connection Banishment〉/ [PR #23](https://github.com/cardinal-sys/Release_Recollection_Cardinal/pull/23) 〈Fifth Profile Awakening〉) を 50キー〈Administrator〉側へ一括同期。**(1) Apple HID Interval Compat**: Apple 系 BLE (macOS/iPadOS/iOS) が `MIN_INT=MAX_INT=6` (7.5ms 固定要求) を範囲狭すぎとして拒否しデフォルト ≈30ms に転落する仕様回避のため、`BT_PERIPHERAL_PREF_MAX_INT` を `6 → 12` (15ms 上限) に緩和。 7.5〜15ms の範囲指定で Apple から最低 15ms を引き出し、Win/Android は引き続き 7.5ms 最速。左右両刀 (Night_Sky_Sword / Blue_Rose_Sword) 完全同期。**(2) Phantom Connection Banishment**: `config/keymap/20_macros.dtsi` に `bt_solo_0..4` の 5 マクロを追加し、各々 `&bt BT_SEL N` 直後に他 4 profile への `&bt BT_DISC` を連射する構造で BLE 帯域奪い合いを封印。 `config/keymap/layers/06_bluetooth.dtsi` の `&bt BT_SEL 0..4` を `&bt_solo_0..4` へ置換。**(3) Fifth Profile Awakening**: ZMK central の `ZMK_BLE_PROFILE_COUNT = CONFIG_BT_MAX_PAIRED - CONFIG_ZMK_SPLIT_BLE_CENTRAL_PERIPHERALS` 仕様により旧 `BT_MAX_PAIRED=5` (`= 5 - 1 = 4`) では profile 4 が不存在で BT 5 (`bt_solo_4`) が `-ERANGE` で沈黙する症状を、ZMK 公式 `app/src/split/bluetooth/Kconfig.defaults` の split central 既定値 `BT_MAX_CONN=6` / `BT_MAX_PAIRED=6` への追従で浄化。 `PROFILE_COUNT = 6 - 1 = 5` で profile 0..4 全 5 枠が蘇生。左右両刀同期。Cardinal 側で GHA build 全成功 + 実機 BT 接続確認通過後に同期申請。双子リポが再び対称構成へ復帰し、〈Cardinal〉と〈Administrator〉双剣の無線輪が同調する。 |
| 2026-05-26 | 〈Noise Cancellation Re-Awakening · Administrator Sync〉— 42キー Cardinal 側 [PR #19](https://github.com/cardinal-sys/Release_Recollection_Cardinal/pull/19) で先行検証された〈Noise Cancellation Re-Awakening〉を 50キー〈Administrator〉側にも同期。`config/west.yml` の `zmk-pmw3610-driver` revision を `60a0782` (cpi-layers のみ) → `35f2c40` (〈Noise Cancellation & Adaptive Precision〉実装 + device tree bindings) へ前進。IIR フィルタ (alpha=614 ≈ 0.6, *1024) を driver default 値で自動有効化し、トラックボール出力のジッターを除去する濾波器を蘇らせる。〈Adaptive Precision〉(speed-based-cpi) は driver default false により **意図的に無効** とし、過去 Run #25889602860 で BT 接続崩壊の主犯候補だった SPI レジスタ書換連発を回避。Cardinal 側で GHA build 全成功（Elucidator/Dark_Repulser/settings_reset 全ターゲット）+ 実機 BT 安定検証（左右接続・5 プロファイル切替・スリープ復帰・ジッター除去体感）通過の確認後に同期申請。双子リポが再び同一ドライバ pin (`35f2c40`) を共有する対称構成へ復帰し、〈Cardinal〉と〈Administrator〉双剣の濾波器が同調する。 |
| 2026-05-26 | 〈Phantom Sigil Pruning II〉— 〈Phantom Sigil Pruning〉(2026-05-25) で README 表からは剪定したものの取り残されていた `keymap_drawer.yaml` の `raw_binding_map` から、`lt_to_layer_0` / `lt_mkp` / `mod_mkp` / `dragkey` / `g_shft` / `lm` の 6 エイリアスを剪定。これら dead code は `keymap.yaml` (draw-keymap.yml で自動再生成) で 0 回参照のため描画への実害はゼロ、純粋な残骸ラベルの除去。双子リポ（42キー Cardinal・50キー Administrator）で同時剪定。dead code 本体 (`config/keymap/30_enhance_armament_base.dtsi` の behavior 定義) は依代として温存。〈Phantom Sigil Pruning〉と合わせ、ドキュメント・描画ラベル両系統から幻影印璽が消滅した。 |
| 2026-05-25 | 〈Phantom Sigil Pruning〉— Hold-Tap Behavior Matrix から実装で完全に 0 usage となっていた `lt_mkp` / `mod_mkp` / `dragkey` の 3 行を剪定し、現役 `gesture_mo_kp` の 1 行に絞った。〈Handling Refine〉(2026-05-01) で導入された hold-tap チューニングが〈Handling Stabilize〉(2026-05-01) の home-row mod (`hm_l`/`hm_r`) 廃止後も「保持」のまま README 表に残留し、双子リポ（42キー Cardinal・50キー Administrator）共通の幻影印璽として漂っていた。dead code 本体 (`config/keymap/30_enhance_armament_base.dtsi` の behavior 定義) は将来再昇華に備えた依代として温存。剣士が手にする現役神器のみが矩形（マトリクス）に映る世界像へ復帰した。 |
| 2026-05-25 | 〈Pathname Sovereignty〉— 〈Sigil Vault Partition〉適用後も「Administrator Editor で `config/Administrator.json` が 404 になり Visual Editor の物理レイアウトが崩壊」する症状が継続したため、ブラウザの form autofill（再訪時に input value を復元する Chrome の挙動）が古い `Release_Recollection_Cardinal` を復元し続けている疑いを断つべく、URL pathname から repo を**直接導出**する〈Pathname Sovereignty〉を追加。`editor/app.js` に `deriveRepoFromUrl()` / `expectedRepo()` / `isRepoSovereign()` を新設し、`window.location.hostname.endsWith('.github.io')` の場合は `cardinal-sys/Release_Recollection_<エディタ名>` を URL から強制導出。state 初期値 / loadCredentials / handleAuth の全経路で sovereign repo を優先採用し、repo input は readonly 化＋title tooltip で固定理由を明示。localStorage に汚染された repo 値が残っていれば自動掃除。ローカル開発（localhost / file://）では従来通り input を尊重するため Tauri デスクトップ版や `python3 -m http.server` でも互換性維持。これにより GitHub Pages デプロイ版は **どんな漏れ込みでも URL が支配する**鉄則を獲得した。 |
| 2026-05-25 | 〈Cardinal Mirror Reflection〉— Visual Editor (`Administrator.json`) と実機物理 (`Administrator.dtsi`) で 0.5 unit 乖離していた右 thumb cluster (pos 47/48) の座標を完全同期。〈Right Thumb Widening II〉(2026-05-24) を含む歴代 3 度の widening 儀式（〈Thumb Cluster Widening〉→〈Thumb Cluster Cardinal-fication〉→〈Right Thumb Widening II〉）がいずれも JSON 側にのみ刻まれ、DTSI は Phase 1 鋳造時の座標で凍結されていた。`pos 47: x=750→800, rx=650→850, ry=387→437` / `pos 48: x=863→913, rx=0→963, ry=350→400`。特に **pos 48 の rx=0** は rotation center が原点固定の異常値で、ZMK Studio 描画時に thumb 回転中心が破綻していた潜在不具合を解消。`col-gpios`/`row-gpios` 等の電気的接続は不変につき、実機キー入力動作には影響しない。Cardinal Editor の Visual Editor と ZMK Studio の両描画系が初めて同一の物理像を共有し、双剣の右翼が真の鏡面対称を取り戻す。 |
| 2026-05-25 | 〈Sigil Vault Partition〉— Administrator Editor (50キー版) と Cardinal Editor (42キー版) が共通の `localStorage` キー (`cardinal_editor_repo` 等) を使っていたため、片方の `repo` 値がもう片方のセッションに漏出して GitHub API への fetch が 404 を返す混線を封印。`editor/app.js` の `STORAGE_KEYS` をエディタ識別子 (`__administrator_50` / `__cardinal_42`) で suffix 化し、PAT / repo / branch / remember 設定すべての記憶領域を分割。既存ユーザの利便のため `migrateLegacyCredentials()` を追加し、旧キーから PAT と Remember 設定だけは新キーへ昇華 (`repo`/`branch` は引き継がず混線源を断つ)。両エディタの `editor/app.js` に対称的な変更を施し、SAO 風には〈Sigil 保管庫〉を Cardinal Cardina と Administrator Quinella の名で隔壁分離した儀式に相当する。報告された症状は「Administrator Editor で `config/Administrator.keymap` 等が 404 になり編集できない」で、原因は localStorage に残っていた `cardinal-sys/Release_Recollection_Cardinal` を Administrator Editor が誤って参照していたこと。今後はエディタ切替時にも localStorage が干渉しない。 |
| 2026-05-25 | 〈Pillar Symmetry Restoration〉— window_min コンボ（Gui+M）の相方を `pos 50` から `pos 49` へ修正し、三神器コンボ Gui+Q (pos 10+24) / Gui+W (pos 24+38) / Gui+M (pos 38+49) を全て **col 13 縦並び隣接** で対称化。先の〈Outer Pillar Realignment〉(2026-05-24) にて pos 49 ↔ 50 を入替し DEL を外柱（col 14）へ移送した副作用として、window_min のみ col 13→col 14 斜め配置で残置され Q/W との pillar 整合性が崩れていた。本修正により Cmd+Q / Cmd+W / Cmd+M の Mac OS 三神器（quit / close window / minimize）が物理的にも一本柱として整列し、右手最内列の押下感覚で三者を直感的に呼び出し可能に。`config/keymap/10_combos.dtsi` の `key-positions = <38 50>` → `<38 49>` の 1 行のみ。 |
| 2026-05-25 | 〈Cardinal System Reawakening〉— 双子の原典 42キー版 Cardinal で先行実施された改名儀式を 50キー版〈Administrator〉にも適用し、`administ-rator`（最高司祭 Quinella の称号「Administrator」を hyphen sigil で封印した真名）を退け、Underworld 原典管理 AI〈Cardinal System〉の略号 `cardinal-sys` へ GitHub username を再封名した儀式の同期記録。「Cardinal が原典・Administrator がその系列下の簒奪派閥」という Alicization 編本来の上下構造を、皮肉にも〈Administrator〉を冠する 50キー版リポジトリの account 階層にも反映する。手順は Cardinal 側の (a) 抜け殻退避 → (b) `administ-rator` → `cardinal-sys` rename → (c) GitHub 自動 redirect で旧 URL 保全、までを既に完了済みのため、本リポジトリでは reference 同期のみを実施。`config/west.yml`（remote 名 `administ-rator` → `cardinal-sys` + 2 project の remote: zmk-pmw3610-driver / zmk-mouse-gesture）/ `Administrator.zmk.yml`（URL）/ `Night_Sky_Sword.conf`（PMW3610 driver コメント）/ `CLAUDE.md`（姉妹リポ参照 + ドライバ参照 + proxy URL + ドライバ改修フロー + ビルド確認 × 2 の計 6 行）/ `editor/index.html` `editor/app.js`（default repo input）/ `src-tauri/tauri.conf.json` `src-tauri/Cargo.toml`（identifier `com.administ-rator.cardinal-editor` → `com.cardinal-sys.cardinal-editor` と authors）/ `scripts/install_launchd.sh` `uninstall_launchd.sh`（PLIST_NAME 同期）/ `LICENSE`（Copyright 表記）/ README `EQUIPPED MODULES` 表 2 行・GitHub Pages URL 2 行を新名へ追従、git remote URL も `cardinal-sys/Release_Recollection_Administrator` へ更新。Tauri identifier と launchd PLIST_NAME 同期更新の副作用として既存インストール済みアプリは新 identifier 扱いとなり旧 launchd service は孤児化する点に留意（必要なら旧 service の手動 unload 推奨）。Cardinal 側既存 SYSTEM LOG 〈Cardinal System Reawakening〉(2026-05-25) と完全対称の儀式記録として刻む。これにより 42キー版 Cardinal と 50キー版〈Administrator〉の双子リポジトリは再び同一 account `cardinal-sys` 配下に統一帰属し、〈Cardinal〉が真の管理者として双剣を共に統括する体制へ復帰した。 |
| 2026-05-24 | 〈Genesis Cascade〉— Phase 1 全完遂（Shield 基盤鋳造・基礎/剣技/レイヤー dtsi 全 31 ファイル移植・50キー matrix 機械マッピング・keymap entry）+ Phase 4 ほぼ全完遂（周辺ファイル・editor/ Cardinal Editor Web GUI・src-tauri/ Tauri デスクトップ版・物理レイアウト 51 keys・README 再編）+ K-α 追加 8 ポジション実用化（Esc/Tab/Shift/Ctrl/BSPC/ENT/Shift/Del）を一気通貫達成。初回 GHA build 全成功（Night_Sky_Sword rgbled_adapter + Blue_Rose_Sword rgbled_adapter + settings_reset）。残るは Phase 2（実機到着後の pin/matrix 検証・PMW3610 微調整）と Phase 3（west.yml ドライバ統合は既配置のため軽量）。 |
| 2026-05-24 | 〈Administrator Awakening〉— Release Recollection 50キー版〈Administrator〉の建立。Cygnus素体（Dist16384/Cygnus-M-Lkeymouse）を仕様参考として、Cardinal版（42キー）の設計思想を継承して新リポを起源化。シールド〈Night_Sky_Sword〉（右手・キリト神器）/〈Blue_Rose_Sword〉（左手・ユージオ神器）の双剣構成。本コミット時点は骨格のみ（README / CLAUDE.md / .gitignore / LICENSE / build.yaml / config/west.yml / zephyr/module.yml / .github/workflows/build.yml）。Phase 1 以降で記憶解放術式の本格移植開始。 |
