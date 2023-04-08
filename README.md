# my-whisper-api-app

ゆるキャラと会話することができます。
OpenAIのgpt-3.5-turbo及びwhisper-1を使用しています。
動作環境はローカルを想定しています
確認できたのはmac(Big Sur)及びwindows10(22H2)です

# 使用前の設定

- あらかじめVOICEVOXをインストールして起動してください
- OpenAIのサイトでAPIkeyを取得し
- conf.pyを作成してそこでOPEN_AI_API_KEYに取得したAPIkeyを記述してください

# 起動

- main.pyを起動すれば会話ができるようになります。
- 停止ワードなど詳細はソースを確認してください
