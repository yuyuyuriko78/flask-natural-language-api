# flask-natural-language-api

## ライブラリのインストール
仮想環境等で以下を実行
```bash
pip install -r requirements.txt
```

## 環境変数の設定
fuga.jsonは、NaturalLanguageAPI用に作成した、GCPサービスアカウントの鍵のJSONファイルである。
#### macOS
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/user/Documents/hoge/fuga.json"
```
#### Windows
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\user\Documents\hoge\key.json"
```

## 実行
```bash
python run.py
```