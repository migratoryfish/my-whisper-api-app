
import wave
import pyaudio
import requests
import json
import time
import io

def text_to_voice(response: str):
    play_wavfile(post_synthesis(post_audio_query(response)))


def post_audio_query(text: str) -> dict:
    params = {'text': text, 'speaker': 1}
    res = requests.post('http://localhost:50021/audio_query', params=params)
    return res.json()

def post_synthesis(audio_query_response: dict) -> bytes:
    params = {'speaker': 1}
    headers = {'content-type': 'application/json'}
    audio_query_response_json = json.dumps(audio_query_response)
    res = requests.post(
        'http://localhost:50021/synthesis',
        data=audio_query_response_json,
        params=params,
        headers=headers
    )
    return res.content

def play_wavfile(wav_file: bytes):
    wr: wave.Wave_read = wave.open(io.BytesIO(wav_file))
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wr.getsampwidth()),
        channels=wr.getnchannels(),
        rate=wr.getframerate(),
        output=True
    )
    chunk = 1024
    data = wr.readframes(chunk)
    while data:
        stream.write(data)
        data = wr.readframes(chunk)
    time.sleep(0.5)
    stream.close()
    p.terminate()
