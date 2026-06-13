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

### ROTARY SIGIL ── EC11 ロータリーエンコーダー（Blue_Rose_Sword / Administrator.dtsi）

*青薔薇の剣の柄に宿る回転の印。一刻みが一拍と同調してこそ、術式は正しく廻る。*

| 設定 | 値 | 効果 |
|---|---|---|
| EC11 steps | 48 | 1 回転あたりの quadrature パルス数（素体 Cygnus `a6429bb` 準拠。旧 12 はパルス数過小で 1 クリックが過剰トリガー化） |
| triggers-per-rotation | 24 | 1 回転あたりのキーマップトリガー数。`48 / 24 = 2 steps/trigger` で 1 デテント = 1 トリガーに正規化 |
| sensor-bindings (L0) | `&inc_dec_kp DOWN_ARROW UP_ARROW` | 回転 1 ノッチごとに ↓ / ↑ を発火 |

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
| 2026-06-13 | 〈Cursor Cadence Wager Withdrawn · iPad Sovereignty〉— 同日試行した BLE 6/6 固定実験（[PR #5](https://github.com/cardinal-sys/Release_Recollection_Administrator/pull/5)〈Cursor Cadence Experiment〉）を**見送り確定**。実機が iPad 主体であることを最優先に据え、6/6 が iPadOS BLE に拒否され ≈30ms へ転落するリスクを許容しない判断。PR #5 をクローズし `feature/cursor-cadence-experiment` ブランチを削除。main は `5a94931`〈EXPERIMENTAL_CONN Dissolution〉(iPad ペアリング修正) + 接続インターバル `6/12`(Apple HID 互換) + エンコーダー 48/24 の **iPad 対応安定構成**を堅持する。カーソル平滑化を追う場合は Win/Android 専用運用が前提となるため、本実験の着想は将来そうした分岐が生じた際に `feature/` で再召喚し得る。同日の〈Rotary Sigil Recalibration〉(EC11 48/24) は main 採用・ビルド成功済で本撤回の影響を受けない。 |
| 2026-06-13 | 〈Cygnus Resonance · Rotary Sigil Recalibration〉— 素体 Cygnus（[Dist16384/Cygnus-M-Lkeymouse](https://github.com/Dist16384/Cygnus-M-Lkeymouse)）の 2026-06 月次更新 4 件（`af469d8` keymap / `f076677` Cygnus_R.conf / `5d0bb32` `a6429bb` Cygnus.dtsi）を観測し、〈Administrator〉への適用可否を精査した儀式。**採用 (1) Rotary Sigil Recalibration** (`a6429bb` 準拠): `Administrator.dtsi` の EC11 を `steps 12 → 48` / `triggers-per-rotation 10 → 24` へ再調律。旧 12/10 は Phase 1.1 鋳造時の素体コピーで、1 トリガー = 1.2 パルスという端数比のため 1 デテントで過剰・不規則トリガーが発生し得た。48/24（2 steps/trigger）で 1 クリック = 1 トリガーに正規化され、青薔薇の剣のエンコーダーが正しい拍で廻る。**不採用 (2) BLE 接続インターバル 6/6 固定** (`f076677`): 素体は `PREF_MIN/MAX_INT=6`（7.5ms 固定 ≈133Hz）でカーソル平滑化を図るが、〈Administrator〉は 2026-05-27〈Bilateral BLE Trinity〉で 6/6 が Apple 系 BLE に拒否され ≈30ms へ転落する症状を確認済。一度 `feature/cursor-cadence-experiment` ブランチ（[PR #5](https://github.com/cardinal-sys/Release_Recollection_Administrator/pull/5)）で実機検証を試みたが、**実機が iPad 主体のため iPad 接続の確実性を最優先し見送り確定**（PR クローズ・ブランチ削除）。main は `6/12`（7.5〜15ms）の Apple HID 互換を堅持する。素体がコメント提案に留めた `PREF_LATENCY=0` も当方は実装済で先行。**不採用 (3) physical layout 回転原点修正** (`5d0bb32`): 素体は右親指キーの `rx=0` 誤記（回転原点が盤面原点に飛ぶ）を修正したが、〈Administrator〉は独自50キー配列で回転キー全数が rx/ry 非ゼロ＝同バグ非該当（かつ描画専用で打鍵無関係）。**不採用 (4) ホームロー A/S の layer-tap 撤去** (`af469d8`): 素体作者の個人キーマップ嗜好であり、〈Administrator〉の A/S は独自の `gesture_mo_kp`（SWORD SKILLS 剣技起動）が憑依済みのため対象外。 |
| 2026-05-31 | 〈EXPERIMENTAL_CONN Dissolution〉— iPad ペアリング時に「デバイス名が消える」（iPadOS が接続ネゴシエーション失敗後にリストから削除する）症状への対処として `Night_Sky_Sword.conf` から `CONFIG_ZMK_BLE_EXPERIMENTAL_CONN=y` を撤去。同フラグは ZMK 実験的な接続パラメータ交渉実装で MacBook とは機能するが iPadOS の厳格な BLE スタックとの互換性が保証されない。MacBook への影響は接続タイミングが若干変わる可能性あり。ビルド後 iPad との接続可否を検証予定。 |
| 2026-05-31 | 〈Live Sync Conduit Truename Hardening · Serializer Root Purge〉— 前項〈BT Disc Sigil Zero-Cell Restoration〉(`50a2384`) は `editor/app.js`（Cardinal Editor の手動 Behavior Picker）を直したが、**実際に GitHub へ書き戻す Live Sync Conduit の本体は `editor/live.js` の `_bindingToZmk()`** であり未修正だったため、次の〈Memory Inscription〉(`3b018c7`) が `&bt_disc_N 0` を再度刻みビルドが再失敗（Run #26698960611）。`live.js` を全面 truename 修正し、Live Sync の多重破損を根治。**(1) bt_disc ゼロセル登録** — `CUSTOM_BEHAVIOR_PARAMS` / `LABEL_TO_NODE` に `bt_disc_0..4`（paramCount=0）を追加し、default 経路の余分な `0` 付与を封印（ビルドエラー根治）。 **(2) Mod-Tap 修飾の真名復元** — `_modMaskToZmk(p1)` が ZMK Studio の HID modifier usage（`0x000700E0..E7`）を ZMK modmask ビット列と誤読し `&mt LEFT_SHIFT Q` を `&mt RG(RA(RS(LEFT_CONTROL))) Q` に化けさせていた（全レイヤー12件）症状を、`_p2ToKc(p1)`（`KBD_MAP[225]=LEFT_SHIFT`）へ切替えて浄化。 **(3) implicit modifier 保持** — `_p2ToKc` が上位バイトの implicit mod を捨て `&gesture_mo_kp 5 LG(LBKT)` を `LEFT_BRACKET` に脱落させていた症状を、`MOD_FN` ネスト復元で修正。 **(4) keypad 真名復元** — `KBD_MAP` に keypad（`0x53..0x63`: `KP_NUMBER_0..9`/`KP_DOT`/演算子）を追加し `&kp 0x0059` 等の生 hex 化（30件）を `&kp KP_NUMBER_1` 等へ復元。 **(5) UTF-8 文字化け根治** — 既存ファイル読込の `atob()` 単体を書込側 `btoa(unescape(encodeURIComponent()))` と対称な `decodeURIComponent(escape(atob()))` へ修正。これが em-dash「—」・日本語コメントが同期毎に多段化け（`—`→`â`→`Ã¢ÂÂ`）していた根本原因。 合わせて全 17 レイヤーのヘッダコメントを最後の手書き正常版 `ba25a6b` から復元（バインド不変を検証）。 検証: Node で実 `_bindingToZmk`/`_p2ToKc` を mock 駆動し Mod-Tap 修飾・implicit mod・bt_disc ゼロセル・keypad・UTF-8 ラウンドトリップの 8 ケース全合格。 実機（ZMK Studio）が真のキーマップのため、`live.js` デプロイ後に実機から再同期すれば全レイヤーがクリーンな dtsi で再生成される。 双子リポ（42キー Cardinal）にも同 serializer 修正を計画。 |
| 2026-05-31 | 〈BT Disc Sigil Zero-Cell Restoration · Live Sync Purge〉— Live Sync Conduit〈Memory Inscription〉(`f137025`) が `config/keymap/layers/06_bluetooth.dtsi` の `&bt_disc_0..4` (`#binding-cells = <0>` の純ゼロセルマクロ) に余分な `0` 引数を付加し `&bt_disc_N 0` として書き戻したため、devicetree パーサが末尾の `0` を独立 phandle として解釈し `error: 'DT_N_S_keymap_S_bluetooth_P_bindings_IDX_21_PH_FULL_NAME' undeclared` で Night_Sky_Sword rgbled_adapter ビルドが失敗（Run #26698596978 / Phase: `West Build` で停止）。 修正: **(1) 応急浄化** — `06_bluetooth.dtsi` の 5 箇所 `&bt_disc_N 0` を `&bt_disc_N` へ復元しビルド即復旧。 **(2) Serializer 再発封印** — `editor/app.js` Behavior Picker (`bpSetBehavior` / `bpBuildString`) の `noArgBehaviors` リストに `&bt_disc_0` 〜 `&bt_disc_4` を追加し、引数 UI を非表示化することで「raw 入力フォームの既定値 `0` が末尾に混入する」経路を封じた。 〈BT Disc Sigils〉が再びゼロセル真名 (`&bt_disc_N` 単体) でレイヤーに刻まれ、〈Memory Inscription〉再実行時の同種破損を予防する。 双子リポ（42キー Cardinal）に同症状が再現する場合は同等の serializer 修正を計画。 |
| 2026-05-29 | 〈BT Disc Sigils Awakening〉— 複数接続によるトラックボール遅延対策として `bt_disc_0..4` マクロを新設。`bt_disc_N` は `BT_SEL N` 切替後に他 4 プロファイルへ `BT_DISC` を連射し不要な同時接続を強制切断する。`bt_solo_0..4` マクロを廃止し上段を `&bt BT_SEL 0..4` 直書きへ昇華。`bt_pair_0..4` マクロも廃止（新規ペアリングは上段の純 BT_SEL を使う）。レイヤー構成: 上段 = `BT_SEL`（純切替・新規ペア兼用）、中段右 = `bt_disc`（遅延対策用）。 |
| 2026-05-29 | 〈Full Behavior Arsenal · Twin Sync〉— Layer Editor の behavior ドロップダウンを ZMK Studio 全 behavior に拡張し、42キー版へ双子同期。新規追加: `&sk`（Sticky Key）/ `&kt`（Key Toggle）/ `&key_repeat`（Key Repeat）/ `&tog`（Toggle Layer）/ `&to`（To Layer）/ `&sl`（Sticky Layer）/ `&gresc`（Grave/Escape）/ `&bt`（Bluetooth コマンド選択）/ `&out`（Output Selection: OUT_AUTO/USB/BLE）/ `&ext_power`（EP_OFF/ON/TOG）/ `&bootloader` / `&sys_reset` / `&studio_unlock`。これにより Layer Editor の behavior カバレッジが ZMK Studio と同等になり、カスタム入力を使わずほぼ全キーを選択式で設定できるようになった。 |
| 2026-05-29 | 〈Layer Binding Rewrite · Twin Sync〉— Cardinal Editor（`editor/index.html` / `app.js`）に `layers/*.dtsi` の**選択式ビジュアルエディター**を建立し、42キー版〈Cardinal〉へも双子同期。ファイルツリーで `00_default.dtsi` 等のレイヤーファイルを開くと `[ Layer Editor ]` ビューが有効化され、物理レイアウト上でキーをクリック → behavior ドロップダウン（`&kp` / `&mt` / `&lt` / `&mo` / `&gesture_mo_kp` / `&smart_num` / `&ht_snipe` / `&mkp` / `&td_enter` 等）でカテゴリ別セレクター入力 → Apply → dtsi バインド形式で即時書き戻し → Seal & Commit で実機ビルドへ反映する一貫フローを確立。これにより `keymap.yaml`（表示用）ではなく**ファームウェアのソースを直接選択式で編集**できるようになった。合わせてヘッダーに **🔑 Change PAT ボタン**を追設し、PAT 期限切れ時にクリック一発で PAT クリア＆再認証フォームへ戻れるようにした（`[404] Not Found` Sealing 失敗への対処）。 |
| 2026-05-28 | 〈BT Solo Sigils · Pure Switch〉— `bt_solo_0..4` マクロから `&bt BT_DISC` 連射を撤去し、純粋な `&bt BT_SEL N`（プロファイル切替のみ）へ変更。 旧版〈Phantom Connection Banishment〉では各 `bt_solo_N` が `BT_SEL N` 直後に他 4 profile へ `BT_DISC` を連射し非アクティブ profile を強制切断していたが、**(1)** プロファイル切替のたびに他の接続中ホストまで切断してしまう副作用、**(2)** ペアリング進行中に押すと新規 bond 確立を破壊し「2台目以降ペア不可」を招く副作用、が大きく「無線が変になった」原因となっていた。 `config/keymap/20_macros.dtsi` の `bt_solo_0..4` の `bindings` を `<&bt BT_SEL N>` 単発へ簡約（BT_DISC 行を全除去）。 これにより `bt_solo_N` と `bt_pair_N` は等価（共に純 BT_SEL）になり、プロファイル切替で他機器が切れず、どのキーでも新規ペアリングを壊さない。 ヘッダコメントも実態に合わせ更新（旧 BT_DISC 経緯は履歴として温存）。 複数ホスト同時接続の BLE 帯域奪い合い（トラックボール遅延）が再発する場合は `&bt BT_DISC` を個別運用で対処する方針。 双子リポ（42キー Cardinal）にも対称同期。 |
| 2026-05-28 | 〈Bond Overwrite Sanction Revert · Passkey Banishment〉— 〈Bond Overwrite Sanction〉(`651a2ea`) で追加した `CONFIG_ZMK_BLE_EXPERIMENTAL_SEC=y` を **revert**。 `EXPERIMENTAL_SEC` は bond 上書き許可だけでなく **BT Secure Connection のパスキー入力も有効化**するため、ペアリング時にホスト側へ 6 桁のパスキー番号が表示され、それをキーボードで入力する必要が生じる挙動に変わった（「番号が出る・変になった」の正体）。 利用者はこのパスキー方式を望まないため `Night_Sky_Sword.conf` から SEC フラグを撤回し、従来のパスキー不要ペアリングへ復帰。 `CONFIG_ZMK_BLE_EXPERIMENTAL_CONN=y`（接続安定性）は維持。 新規ペアリング不可問題への別アプローチ（プロファイル消去手順 `&bt BT_CLR` の運用、または passkey を伴わない bond 上書き手段）は今後別途検討。 双子リポ（42キー Cardinal）の同フラグも対称 revert。 |
| 2026-05-28 | 〈Serializer Truename Hardening · Memory Inscription〉— 〈Memory Inscription Rollback〉(`a268d73`) で破損レイヤーを復元したが、**根本原因の live.js シリアライザ自体は未修正**で「Memory Inscription を再実行すれば同じ破損が再発する」状態だったため、`editor/live.js` の `_bindingToZmk()` を恒久修正し再発を封印。 修正内容: **(1) ZMK 標準 behavior の真名変換** — switch で取りこぼしていた `Mouse Move`/`Mouse Scroll`/`Bluetooth` を新マップ `BUILTIN_NODE_TO_ZMK` で正規化ノード名（`mouse_move`/`mouse_scroll`/`bluetooth`）からラベル alias（`&mmv`/`&msc`/`&bt`）へ確実に変換（ZMK Studio が friendly displayName を返しても node 名へ正規化後に捕捉するため大文字小文字に頑健）。 **(2) `&bt` コマンドエンコード** — `app/include/dt-bindings/zmk/bt.h` の enum（`BT_CLR=0`/`BT_NXT=1`/`BT_PRV=2`/`BT_SEL=3`/`BT_CLR_ALL=4`/`BT_DISC=5`）を `BT_CMD` 定数 + `_btToZmk(p1,p2)` で実装。param1=コマンド・param2=引数で、`BT_SEL`(3)/`BT_DISC`(5) のみ profile 引数を付与（例: `&bluetooth 0`→`&bt BT_CLR`、`&bluetooth 4`→`&bt BT_CLR_ALL`、`(3,2)`→`&bt BT_SEL 2`）。 **(3) ゼロセルマクロの引数抑止** — `CUSTOM_BEHAVIOR_PARAMS` に `bt_solo_0..4`/`bt_pair_0..4`/`drag_on`/`drag_off`/`safari_reload_once` を paramCount=0 で登録し、default 経路の「p2=0 なら 1 引数」フォールバックが余分な `0` を付ける挙動を封印（`arrows_alt`=1 も明示登録）。 検証: preview 内で実 `_bindingToZmk` を mock 駆動し、Mouse Move/Scroll の packed 値・`&bt` 全コマンド・ゼロセルマクロ全種・既存の `&td_enter`/`&gesture_mo_kp` 回帰の計 15 ケースで期待出力を確認。 これにより〈Memory Inscription〉(Live Sync→GitHub) が今後 build 可能な dtsi を出力するようになり、双子リポ（42キー Cardinal）にも同期。 デバッグ用に `_bindingToZmk` を `window.__cardinal_live` bridge へ露出（シリアライザ再破損時の検証用）。 |
| 2026-05-28 | 〈Memory Inscription Rollback · All Layers〉— 〈Truename Reference Restoration〉(`f0101f1`) で `00_default.dtsi` の `&tap_dance_enter` を直した後も build が `/keymap/MOUSE: undefined node label 'mouse_move'` で失敗継続したため全容調査した結果、Live Sync〈Memory Inscription〉が **全 17 レイヤー (00〜16) の bindings 行を機械再シリアライズし、複数系統のバグを全レイヤーに刻んでいた**ことが判明: **(1) ノード名をラベル代わりに使用** — `&mouse_move`(→`&mmv`) / `&mouse_scroll`(→`&msc`) / `&bluetooth`(→`&bt`) / `&tap_dance_enter`(→`&td_enter`)、**(2) 引数ゼロのマクロに余分な `0`** — `&bt_solo_N 0` / `&bt_pair_N 0` / `&drag_on 0` / `&drag_off 0` / `&safari_reload_once 0`、**(3) `&bt` の不正エンコード** — `&bluetooth 0` / `&bluetooth 4` (本来 `&bt BT_SEL N` 形式)。 確認した範囲 (mouse 等) では Inscribed 版は同一バインドの round-trip でありキーマップ設計自体は不変だったため、個別パッチ (17 ファイル × 複数バグ種・取りこぼしリスク) ではなく **最後の手書き正常版 `ba25a6b` から全 17 レイヤーを一括復元** する rollback を選択。 `git checkout ba25a6b -- config/keymap/layers/` で 00〜16 を復元し、grep で破損参照 (ノード名・余分 0 引数) がゼロになったことを確認。 復元後の各レイヤーは Pure Pairing の `bt_pair`/`bt_solo` 配置・Col-Offset 修正など直近の正規作業を全て含む設計済みキーマップで、firmware build が復旧する。 Inscribed 版は git 履歴 (`9ca2baa`) に温存され後から復旧可能。 根本原因の live.js シリアライザ (ノード名→ラベル変換の不完全さ・ゼロセル behavior への 0 引数付与) は別途〈Modifier Sigil Truename Awakening〉系の live.js 改修で恒久対処予定 (現在未コミット保留中の WIP に含む)。 |
| 2026-05-28 | 〈Truename Reference Restoration · Default Layer〉— `9ca2baa`〈tap_dance_enter → td_enter〉が live.js シリアライザ（`LABEL_TO_NODE` マップ）を直したものの、**既に commit 済みの破損 `00_default.dtsi` 自体は未修正**だったため GHA build が `devicetree error: /keymap/default_layer: undefined node label 'tap_dance_enter'` で失敗し続けていた症状を浄化（Run #26559009404 / Night_Sky_Sword rgbled_adapter ほか全 shield job が `dts.cmake` の `Child return code: 1` で停止）。 原因: Live Sync の〈Memory Inscription〉が tap-dance behavior をシリアライズする際、ZMK Studio `getBehaviorDetails` が返す `displayName='tap_dance_enter'`（**ノード名**）を `&tap_dance_enter` と書き出していたが、ZMK devicetree が keymap で解決できるのは label alias `&td_enter` のみ（定義: `config/keymap/00_prelude.dtsi:47` の `td_enter: tap_dance_enter { compatible = "zmk,behavior-tap-dance"; ... }`）。 `9ca2baa` の live.js 修正は**今後**の Memory Inscription が正しい `&td_enter` を吐くようにする予防策で、過去に刻まれた破損ソースには遡及しないため、build を通すには破損 dtsi の直接浄化が別途必要だった。 修正: `config/keymap/layers/00_default.dtsi:7` の唯一の破損参照 `&kp BACKSPACE  &tap_dance_enter  &kp DELETE` を `&kp BACKSPACE  &td_enter  &kp DELETE` へ書換（全 config/ を grep し他レイヤーに破損参照が無いことを確認済み）。 これにより default_layer の tap-dance（長押し=L1 / 1タップ=Shift+Enter / 2タップ=Enter）が label alias で正しく解決し、firmware build が復旧する。 |
| 2026-05-28 | 〈Live Inscription Awakening〉— Cardinal Editor（`index.html` / `app.js`）に**自動封印術式〈Live Inscription〉**を建立。ファイル編集（コードエディタ入力・Visual Editor キー書換・Combos/Macros/Behaviors/Gestures/Settings 各ビジュアルエディタ操作）を検知し、デフォルト **3秒のデバウンス**後に `commitAll()`（Git Tree API 一括コミット）を自動発火する。右パネル SEALING セクションに〈LIVE INSCRIPTION〉サブパネルを追設し、**トグルボタン**（`[ Auto-Sync: OFF ]` ⇔ `〈 Auto-Sync: ON 〉`）・カウントダウン表示・最終封印時刻・デバウンス値変更ボタンを配置。ON 時はゴールドアクセントで脈動アニメーション、pending 時はリアルタイムカウントダウン、コミット中は点滅、成功後は `✅ 最終封印: HH:MM:SS` を表示する。**`Ctrl+S` / `⌘S`** でのワンクリック即時封印も追加（Auto-Sync ON 時はデバウンス待機をバイパスして即時発火、OFF 時は従来の Seal ダイアログを起動）。`autoSync` state オブジェクト（enabled / debounceMs / timer / countdown / remaining / lastCommitAt / inFlight）と `autoSyncOnChange()` / `triggerAutoSync()` / `toggleAutoSync()` / `updateAutoSyncUI()` の 4 関数で完全に独立したエンジンを構成。既存の手動 Seal フローへの影響ゼロ。同時に Live Sync Conduit（`live.html` + `live.js`）の**GitHub Sync 機能**（前回実装）も main へ合流：ZMK Studio キーマップ JSON → DTSi 変換エンジン・Git Tree API 一括コミット・`live.html` 内 GitHub Sync パネル（PAT/Branch/CommitMsg/ステータス）が正式リリース。 |
| 2026-05-28 | 〈Memory Inscription Awakening〉— Live Sync Conduit（`live.html` + `live.js`）で取得した ZMK Studio キーマップ JSON を、**ブラウザから GitHub API を直接呼び出して**リポジトリへコミット・同期する機能を建立。ローカルサーバ等の追加ツール一切不要、GitHub Pages 上の `live.html` からそのまま動作する。`live.js` 内に ZMK Studio binding JSON → ZMK DTSi 変換エンジン（`_bindingToZmk()` / `keymapToDtsiFiles()`）を実装し、Key Press / Mod-Tap / Layer-Tap / Momentary Layer / Toggle Layer / Sticky Key / Sticky Layer / Mouse Key Press / Consumer / Output Selection / External Power 等の主要 behavior に全対応、implicit modifier ビット（`LS()` / `LC()` 等）も展開する。各レイヤー `.dtsi` ファイルの既存ヘッダコメントと `sensor-bindings` は GitHub から先読みして保持したまま、**Git Tree API（blob → tree → commit → ref 更新）で全レイヤーファイルを 1 コミットにまとめて**刻印する（Cardinal Editor の `commitAll()` と同方式）。`live.html` の MEMORY MATRIX セクションに〈GitHub Sync パネル〉（PAT 入力・ブランチ名・コミットメッセージ）を追設し、PAT は `localStorage` に永続保持する。〈Save Changes〉でキーボードへ永続化 → 〈GitHub へ同期〉でリポジトリへも刻印する二段階記憶定着フローを確立。 |
| 2026-05-28 | 〈Modifier Sigil Truename Awakening · Live Editor〉— Cardinal Editor `live.html` (MEMORY REWRITE LIVE パネル) で「Mod-Tap binding を開くと修飾キー (ホールド時) slot の checkbox が意図と無関係な 4 modifier (例: LCtl / RSft / RAlt / RGui) に勝手にチェックが付く」症状を浄化。 原因: ZMK Studio は Mod-Tap の `param1` を **HID page-7 keyboard modifier usage** (`KBD(224..231)` / `0x000700E0..0x000700E7`) として encode する (上流 `zmk-studio/src/behaviors/HidUsagePicker.tsx` の `Mods` enum + `parameters.ts` の `hid_usage_page_and_id_from_usage()` バリデーション `page !== 0 && id !== 0` で確認済み) が、`editor/live.js` の `BEHAVIOR_PARAM_SPEC['Mod-Tap'].p1.type = 'modmask'` および `buildModMaskSelector` が誤って ZMK firmware C macro 階層の modmask bitmask (`MOD_LCTL=0x01 / LSFT=0x02 / LALT=0x04 / LGUI=0x08 / RCTL=0x10 / RSFT=0x20 / RALT=0x40 / RGUI=0x80`) として再解釈し、`current & mask` で checkbox 状態を決めていたため、LSft を意味する `458977 = 0x000700E1` の下位バイト `0xE1` が `LCtl(0x01) | RSft(0x20) | RAlt(0x40) | RGui(0x80)` と偶発的に一致して 4 modifier に check が描画されていた (さらに Apply 時には modmask 値 `0x02` がそのまま送出されるため ZMK Studio 側のバリデーションで `page=0` と判定され弾かれる隠れ症状も伴い、binding が firmware に反映されない事態を招いていた)。 修正: `BEHAVIOR_PARAM_SPEC` に新型 `'hid-modifier'` (HID page-7 modifier usage 単体) を導入し、Mod-Tap `p1.type` を `'modmask'` → `'hid-modifier'` へ転生。新セレクタ `buildHidModifierSelector` は 8 modifier (`LCtl/LSft/LAlt/LGui/RCtl/RSft/RAlt/RGui`) を **単一選択** dropdown として描画し、選択値を HID usage (`KBD(224..231)`) として `bind-param1` へ書き込む。 既存 binding decode は `current` を HID usage 数値として 8 候補と一致比較し、合致する modifier を pre-select (非該当時は `— 選択 —` placeholder を表示し利用者の能動的指名を要求)。 dead code となった `MOD_MASKS` 定数 / `buildModMaskSelector` / `renderSlot` の `case 'modmask'` / `getQuickPickOptions` の `case 'modmask'` は浄化。 〈Type-Matched Inheritance〉(`adaptParamsForNewBehavior`) は `'hid-modifier'` を意図的に `'hid'` と**非互換**型として扱い、Mod-Tap ↔ Key Press 遷移で「修飾キーがタップキー候補に混入する」誤転生を封印 (Mod-Tap → Key Press では旧 `p2=タップキー` のみが新 `p1=hid` へ転生し、旧 `p1=修飾キー` は破棄; Key Press → Mod-Tap では旧 `p1=hid` が新 `p2=タップキー` slot へ流入し、新 `p1=修飾キー` は 0 でクリア)。 これにより上流 ZMK Studio と完全に encoding が同調し、〈Memory Rewrite Live〉が Mod-Tap binding を真名 (true name) で受理・送出する儀式へ収束した。 |
| 2026-05-28 | 〈Param Reincarnation · Live Editor〉— Cardinal Editor `live.html` (MEMORY REWRITE LIVE パネル) で「ホールドタップから通常キーに変更できない」症状を浄化。 原因: `editor/live.js` の binding editor が behavior 切替時に旧 param をそのまま新 spec に流し込んでいたため、Mod-Tap (param1=modmask, param2=hid) → Key Press (param1=hid, param2=none) 遷移で **(a) Slot 2 が `.hidden` にされるだけで `bind-param2` の隠し input には旧タップキー HID が残留**し、Apply 時に `SetLayerBinding(behaviorId=63, param1=Q, param2=Q)` という不整合 binding をファームウェアへ送って弾かれ、**(b) Slot 1 にも旧 modmask が引き継がれて `LSHIFT` が事前選択**されるため利用者が必ず手動で押し直す必要があった。 修正: `renderSlot` の `type==='none'` 分岐で対応する `bind-param1/2` を 0 に浄化する〈Slot Purge〉と、新設関数 `adaptParamsForNewBehavior(oldName, newName, oldP1, oldP2)` で旧 behavior の各 param を `type` 鍵で照合し新 behavior の同型 slot へ再配置する〈Type-Matched Inheritance〉を導入。 これにより Mod-Tap(LShift, Q) → Key Press 遷移で **タップ側 Q が新 param1=hid へ転生し、Slot 2=none は自動的に 0** へ封じられる。 `openBindingEditor` で `state._editorPrevBehaviorId` に開始時の behavior を anchor し、change ハンドラはこれを参照して旧 spec を逆引きする。 検証 (preview 内 mock 駆動): Mod-Tap→Key Press / Key Press→Mod-Tap / Mod-Tap→Layer-Tap / Mod-Tap→Transparent / Mod-Tap→Mod-Tap(自己同一) の 5 系列で `bind-param1/2` が期待通りに転生・浄化されることを確認。 〈Memory Rewrite Live〉が真に直接書換 (`SetLayerBinding + SaveChanges`) を達成し、利用者は behavior を式変換するだけでファームウェアが受理可能な binding を再構築する。 |
| 2026-05-28 | 〈Pure Pairing Sigils Awakening〉— 〈Bilateral BLE Trinity · Administrator Sync〉(2026-05-27) で投入された `bt_solo_0..4` マクロ（〈Phantom Connection Banishment〉由来）が新規ペアリング進行中に Pairing/Bonding シーケンスを破壊し「1台目は pair できるが 2台目以降不可」の症状を引き起こす副作用が実機で表面化。ZMK 公式 `&bt BT_DISC N` は `if it's currently connected and inactive` の条件で active connection を切断する仕様だが、`BT_SEL N` 直後の `BT_DISC` 連射が host 側 securing flow（特に Apple 系の Pairing/Bonding）と race し、advertising 状態下での incoming pair request を取りこぼす挙動を確認。第一手として `bt_solo` 撤回は見送り、新規 host との bond 確立に専念する純粋 `&bt BT_SEL N` 単発マクロ `bt_pair_0..4` を新設して〈Pure Pairing Sigils〉として共存運用へ。 `config/keymap/20_macros.dtsi` に `bt_pair_0..4` 5 マクロ追加（disc 連射なし、`BT_SEL N` のみ）。 `config/keymap/layers/06_bluetooth.dtsi` の Row 1 右側 `&trans` 枠 (positions 8–12) に `&bt_pair_0..4` を配置し、`&bt_solo_0..4` の真下に縦並びでペアリング専用列を建立。 運用規約: 新規 host ペア時は `bt_pair_N` を使用 → bond 確立完了後の日常切替は `bt_solo_N` を使用。 双子リポ（42キー Cardinal）にも同症状があるはずのため、別途〈Pure Pairing Sigils〉同期を計画。 ペアリング層が `bt_pair_N` (新規) と `bt_solo_N` (切替) の二刀流に再編され、〈Administrator〉が真名解放の儀式と日常守護の権能を別個の sigil として行使可能に。 |
| 2026-05-27 | 〈Col-Offset Sovereignty Restoration〉— 50キー版 Administrator 初回実機投入時に全キーが実機と一致しない症状を根本解決。`Blue_Rose_Sword.overlay`（左手・peripheral）に `col-offset = <7>` が誤設定されていたため、左手 7列が cols 7–13（matrix columns=13 を超えた col 13 まで）を主張し、右手 Night_Sky_Sword が cols 0–5 を占有するという左右転倒状態が発生していた。`default_transform` の map は左手 cols 0–6・右手 cols 7–12 を前提とするため、全キーの matrix 座標が対岸ハーフへ完全に投射されるという「双剣逆転の封印」となっていた。修正: `&default_transform { col-offset = <7>; };` を `Blue_Rose_Sword.overlay` から撤去し `Night_Sky_Sword.overlay` へ移植。これにより左手 peripheral が cols 0–6（7列）・右手 central が cols 7–12（6列）を管轄する正規配置へ復帰し、全 51 バインドが実機物理キーと一対一で対応する。Cardinal 版（Elucidator に col-offset=6、Dark_Repulser はオフセット無し）と同一の設計規約に収束。 |
| 2026-05-27 | 〈Twin Symmetry Restoration · Administrator Sync〉— Cardinal 側〈Twin Symmetry Restoration〉と対称の Admin 側 doc 修正。 双子同期監査で発覚した最後の残響: `config/keymap/00_prelude.dtsi:4` の「Release_Recollection.keymap から最初にインクルードされる。」を「Administrator.keymap から最初にインクルードされる。」へ修正。 〈Cardinal System Reawakening · Administrator Echo〉(2026-05-25) のリネーム儀式で取り残されていた残響を最終的に剪定。 Cardinal 側では同コミットで `20_macros.dtsi` の BT_MAX_CONN 古コメント (5 → 6) 修正と LICENSE 追加 (Admin の MIT を mirror) が同時実施され、双子 (Cardinal / Administrator) の機能・ドキュメント・法務ツリーが対称構成に収束。 |
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
