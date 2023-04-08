# my-whisper-api-app

ゆるキャラと会話できます。  
OpenAIのgpt-3.5-turbo及びwhisper-1を使用  
確認済動作環境はmac(Big Sur)及びwindows10(22H2)です。

# 使用前の設定

- あらかじめVOICEVOXをインストールして起動してください
- OpenAIのサイトでAPIkeyを取得し conf.pyを作成してそこで`OPEN_AI_API_KEY`に取得したAPIkeyを記述してください

# 起動

- main.pyを起動すれば会話ができるようになります。
- 停止ワードなど詳細はソースを確認してください
