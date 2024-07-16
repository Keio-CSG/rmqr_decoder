# Pythonで無理やりrmQRコードをデコードするやつ

# 必要なもの

- 開発者オプションをONにしたAndroidスマホ
- adbコマンド
- tesseractコマンド
- poetry

# 使い方

1. `poetry install`
2. AndroidスマホをPCに接続し、`adb devices`で見えることを確認
3. Androidスマホで[クルクル](https://play.google.com/store/apps/details?id=com.arara.q)を立ち上げておく
4. AndroidスマホのカメラにデコードしたいrmQRコードが写るように配置
5. `poetry run python main.py`
6. デコード結果が標準出力に出てくる

# 流れ

rmQRコード→Androidカメラ→クルクル→adbでアプリをリフレッシュ→スクリーンショット→adbでPCに送信→画像のクロップ→tesseract OCRで文字起こし→出力
