import openai
from chat import chat
from mywhisper_api import voice_to_text
from voicevox import text_to_voice
from conf import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY

def main():
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
    ]
    while True:
        #マイク音声からテキスト出力
        text = voice_to_text()
        #テキストをAPIメッセージに詰める
        messages.append(
            {'role': 'user', 'content': text}
        )
        #APIメッセージを送信
        response = chat(messages)
        #レスポンスをAPIメッセージに詰める
        messages.append(
            {'role': 'assistant', 'content': response}
        )
        print(f'User   : {text}')
        print(f'ChatGPT: {response}')
        #APIにメッセージを投げてレスポンスを音声出力
        text_to_voice(response)
if __name__ == '__main__':
    main()