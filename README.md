# note Web Downloader

note.comの記事をMarkdown形式でダウンロードし、画像も含めてZIPファイルとして配信するWebアプリケーションです。

## 機能

- 🔗 **noteのURL入力**: 記事のURLを入力するだけで簡単ダウンロード
- 📝 **Markdown変換**: HTMLからクリーンなMarkdown形式に変換
- 🖼️ **画像の自動ダウンロード**: 記事内の画像を自動的に取得・保存
- 📦 **ZIP圧縮配信**: 記事と画像をまとめてZIPファイルで配信
- 🚫 **目次除外**: noteの目次機能は対象外として除外
- ✨ **品質向上**: 見出しスペース、強調記号、画像ファイル名などを最適化

## セットアップ

### 必要な環境

- Python 3.8以上
- pip

### インストール手順

1. **リポジトリのクローン**

```shell
git clone <repository-url>
cd note_web_downloader
```

2. **仮想環境の作成と有効化**

```shell
python -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows
```

3. **依存関係のインストール**

```shell
pip install -r requirements.txt
```

4. **アプリケーションの起動**

```shell
python src/main.py
```

5. **ブラウザでアクセス**

    http://localhost:5001

## 使用方法

1. Webブラウザでアプリケーションにアクセス
2. noteの記事URLを入力フィールドに貼り付け
3. 「ダウンロード」ボタンをクリック
4. 自動的にZIPファイルがダウンロードされます

### 対応URL形式

    https://note.com/[username]/n/[article_id]

## 技術スタック

- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS/JavaScript
- **HTML解析**: BeautifulSoup4
- **Markdown変換**: markdownify
- **HTTP通信**: requests
- **データベース**: SQLite (Flask-SQLAlchemy)

## プロジェクト構造

    note_web_downloader/
    ├── src/
    │   ├── main.py              # メインアプリケーション
    │   ├── routes/
    │   │   ├── download.py      # ダウンロード機能
    │   │   ├── health.py        # ヘルスチェック
    │   │   ├── user.py          # ユーザー管理
    │   │   └── debug.py         # デバッグ機能
    │   ├── models/
    │   │   └── user.py          # ユーザーモデル
    │   ├── database/
    │   │   └── app.db           # SQLiteデータベース
    │   └── static/
    │       ├── index.html       # フロントエンド
    │       └── favicon.ico      # ファビコン
    ├── requirements.txt         # 依存関係
    └── README.md               # このファイル

## 実装された機能

### note.com対応

- **記事タイトル抽出**: h1要素からタイトルを取得
- **記事本文抽出**: article要素から本文コンテンツを取得
- **目次除外**: `o-noteEyecatch-tableOfContents`クラスの目次を除外
- **画像処理**: note.comの画像URLに対応した画像ダウンロード

### Markdown品質向上

- **見出しスペース修正**: `#見出し` → `# 見出し`
- **強調記号エスケープ修正**: `\*\*` → `**`
- **画像ファイル名短縮**: 長いファイル名を `image_001.jpg` 形式に変更

### エラーハンドリング

- ネットワークエラーの適切な処理
- 無効なURLの検証
- 画像ダウンロード失敗時の継続処理
- data URLの除外処理

## 開発

### デバッグモード

開発時はデバッグモードで起動されます：

```shell
python src/main.py
```

### ログレベル

詳細なログが出力され、処理の流れを確認できます：

- INFO: 一般的な処理情報
- DEBUG: 詳細なデバッグ情報
- ERROR: エラー情報

## ライセンス

このプロジェクトのライセンスについては、リポジトリ内のLICENSEファイルを参照してください。

## 貢献

バグ報告や機能要望は、GitHubのIssuesでお知らせください。プルリクエストも歓迎します。

## 注意事項

- このアプリケーションは開発サーバーで動作します。本番環境での使用には適切なWSGIサーバー（Gunicorn、uWSGIなど）を使用してください。
- note.comの利用規約を遵守してご利用ください。
- 大量のリクエストを短時間で送信することは避けてください。
