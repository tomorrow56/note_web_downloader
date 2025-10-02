# QiitaダウンローダーWebアプリケーション

## 概要
QiitaのURLを入力して、記事をMarkdown形式でダウンロードできるWebアプリケーションです。画像も一緒にダウンロードし、ZIP形式で圧縮してローカルPCに保存できます。

## 機能
- ✅ QiitaのURL入力フィールド
- ✅ 記事のMarkdown形式変換
- ✅ 画像の一括ダウンロード
- ✅ ZIP形式での圧縮・配信
- ✅ レスポンシブデザイン
- ✅ エラーハンドリング
- ✅ デバッグ機能

## 技術スタック
- **バックエンド**: Flask (Python)
- **フロントエンド**: HTML, CSS, JavaScript
- **主要ライブラリ**: 
  - requests (HTTPリクエスト)
  - beautifulsoup4 (HTML解析)
  - markdownify (HTML→Markdown変換)
  - flask-cors (CORS対応)

## ローカル環境での実行方法

### 1. 環境準備
```bash
# プロジェクトディレクトリに移動
cd qiita_web_downloader

# 仮想環境を作成
python -m venv venv

# 仮想環境をアクティベート
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 依存関係をインストール
pip install -r requirements.txt
```

### 2. アプリケーション起動
```bash
# アプリケーションを起動
python src/main.py
```

### 3. アクセス
ブラウザで http://localhost:5000 にアクセス

## 使用方法
1. QiitaのURLを入力フィールドに貼り付け
2. 「📥 ダウンロード」ボタンをクリック
3. ZIPファイルが自動的にダウンロード開始

## プロジェクト構造
```
qiita_web_downloader/
├── src/
│   ├── main.py              # メインアプリケーション
│   ├── routes/
│   │   ├── download.py      # ダウンロード機能
│   │   ├── health.py        # ヘルスチェック
│   │   ├── debug.py         # デバッグ機能
│   │   └── user.py          # ユーザー機能（未使用）
│   ├── models/
│   │   └── user.py          # ユーザーモデル（未使用）
│   ├── static/
│   │   ├── index.html       # フロントエンド
│   │   └── favicon.ico      # ファビコン
│   └── database/
│       └── app.db           # SQLiteデータベース（未使用）
├── requirements.txt         # 依存関係
└── README.md               # このファイル
```

## API エンドポイント

### メイン機能
- `POST /api/download` - Qiita記事のダウンロード
- `GET /api/health` - ヘルスチェック

### デバッグ機能
- `GET /api/debug/info` - 環境情報の取得
- `POST /api/debug/test-request` - リクエストテスト
- `POST /api/debug/simple-download` - 簡単なダウンロードテスト

## 動作確認済み環境
- ✅ ローカル環境 (Windows/macOS/Linux)
- ❌ デプロイ環境 (WASIX環境で一部制限あり)

## 既知の問題
- デプロイ環境でのダウンロード機能にエラーが発生する場合があります
- 大きな画像が多い記事では処理時間が長くなる場合があります

## トラブルシューティング

### よくある問題
1. **モジュールが見つからないエラー**
   - 仮想環境がアクティベートされているか確認
   - `pip install -r requirements.txt` を再実行

2. **ポートが使用中エラー**
   - 他のアプリケーションが5000番ポートを使用していないか確認
   - `main.py` の `app.run(port=5001)` でポート番号を変更

3. **ダウンロードが失敗する**
   - QiitaのURLが正しいか確認
   - インターネット接続を確認
   - デバッグエンドポイント (`/api/debug/simple-download`) でテスト

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

## 開発者向け情報

### 開発環境のセットアップ
```bash
# 開発用の追加パッケージをインストール
pip install pytest flask-testing

# テスト実行
pytest tests/
```

### デバッグ方法
1. ブラウザの開発者ツールでネットワークタブを確認
2. `/api/debug/info` でサーバー環境を確認
3. `/api/debug/simple-download` で基本機能をテスト

### カスタマイズ
- `src/static/index.html` でUIをカスタマイズ
- `src/routes/download.py` でダウンロード処理をカスタマイズ
- CSS スタイルは `index.html` 内の `<style>` タグで変更

