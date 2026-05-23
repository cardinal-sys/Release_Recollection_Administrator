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

> **[ SYSTEM ]** Live Sync Conduit を使うには Elucidator (central) に ZMK Studio 有効化版ファームウェアが書き込まれている必要がある。Chrome / Edge など Web Bluetooth API 対応ブラウザ必須。

### ◆ 起動方法 ── Invocation

#### 〈オンライン〉GitHub Pages（推奨）

`.github/workflows/deploy-editor.yml` により main ブランチの `editor/` が
自動的に GitHub Pages へデプロイされる。HTTPS なので Web Bluetooth API が
最も安定する。

| 入口 | URL |
|---|---|
| Cardinal Editor (git 編纂) | `https://administ-rator.github.io/Release_Recollection_Administrator/index.html` *（Phase 4 で移植予定）* |
| Live Sync Conduit (実機接続) | `https://administ-rator.github.io/Release_Recollection_Administrator/live.html` *（Phase 4 で移植予定）* |

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
| 神器エントリ | `config/Release_Recollection.keymap` |
| コンボ術式 | `config/keymap/10_combos.dtsi` |
| マクロ術式 | `config/keymap/20_macros.dtsi` |
| Enhance Armament | `config/keymap/30_*` `31_*` `35_*` |
| 剣技（ジェスチャー） | `config/keymap/40_*` 〜 `47_*` |
| 階層（レイヤー） | `config/keymap/layers/*.dtsi` |
| Shield 設定 | `config/boards/shields/Release_Recollection/*` |
| west.yml | `config/west.yml` |

### ◆ 編纂モード ── Edit Modes

- **Code Editor** — CodeMirror による DTS / YAML 構文ハイライト + 括弧マッチング + Active Line Highlight
- **Visual Editor**（`keymap.yaml` 限定）— `config/Release_Recollection.json` のレイアウト座標から **左右分割の物理キーボード配置を再現**。親指列の回転（`r:`）も `transform: rotate()` で忠実に表現。レイヤー切替タブ + キーのクリック編纂で `t:` `h:` を直接書換
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
| `lt_mkp` | balanced | 200 | 150 | 150 | — | マウス層（hold）＋マウスボタン（tap） |
| `mod_mkp` | balanced | 200 | 150 | 150 | — | Shift/Ctrl 用の modifier + mouse-button |
| `dragkey` | tap-preferred | 200 | 100 | 150 | — | ドラッグ専用（マウス + キー同時入力） |

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
| zmk-pmw3610-driver | administ-rator/zmk-pmw3610-driver | PMW3610 トラックボールドライバー |
| zmk-listeners | ssbb/zmk-listeners | レイヤーリスナー |
| zmk-mouse-gesture | administ-rator/zmk-mouse-gesture | マウスジェスチャー認識 |
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
| Experimental Conn | R側(Elucidator)のみ有効、L側無効 | R側（Central） | Central側でホスト向けBLE接続安定化のため有効化 |
| NFCT_PINS_AS_GPIOS | 有効 | R・L両側 | NFC無線とBLEの干渉防止（安定版2つともあり） |
| BT_GAP_AUTO_UPDATE_CONN_PARAMS | 有効 | R・L両側 | 接続後に自動パラメータ再交渉（kabutokoma準拠） |
| BT_CONN_PARAM_UPDATE_TIMEOUT | 1000ms | R・L両側 | 接続から1秒後にパラメータ更新要求 |
| BT_PERIPHERAL_PREF_TIMEOUT | 1000 (10秒) | R・L両側 | ホスト向け接続タイムアウト |
| TX Power | +8dBm | R・L両側 | 最大送信出力 |
| Split BLE Latency | 0 | R側（Central） | デフォルト 30 から 0 へ変更（Left 側キー入力の遅延パケット許容をゼロに） |
| Split BLE Timeout | 1000 | R・L両側 | スプリット接続タイムアウト（両側共通） |
| BT Max Conn | 5 | R側（Central） | 4プロファイル + 1スプリット接続（プロファイル数+1が正しい設定） |
| BT Max Paired | 5 | R側（Central） | プロファイル切替用（Mac/iPhone等） |
| BT_PERIPHERAL_PREF_MIN_INT | 6 (7.5ms) | R側 | 接続インターバル下限。前回MAX_INT=12固定は削除済み→今回は範囲指定で再試験 |
| BT_PERIPHERAL_PREF_MAX_INT | 6 (7.5ms) | R・L両側 | 接続インターバル上限（L側もR側と同期） |
| Insomnia pingInterval | 3秒 | R・L両側 | keepaliveを高頻度化（L側にも追加） |

### MOTION SENSOR CONFIG ── トラックボールセンサー（Elucidator.conf）

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
| EC11スレッド | 4096 bytes | Dark_Repulser | |

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
| 2026-05-24 | 〈Administrator Awakening〉— Release Recollection 50キー版〈Administrator〉の建立。Cygnus素体（Dist16384/Cygnus-M-Lkeymouse）を仕様参考として、Cardinal版（42キー）の設計思想を継承して新リポを起源化。シールド〈Night_Sky_Sword〉（右手・キリト神器）/〈Blue_Rose_Sword〉（左手・ユージオ神器）の双剣構成。本コミット時点は骨格のみ（README / CLAUDE.md / .gitignore / LICENSE / build.yaml / config/west.yml / zephyr/module.yml / .github/workflows/build.yml）。Phase 1 以降で記憶解放術式の本格移植開始。 |
