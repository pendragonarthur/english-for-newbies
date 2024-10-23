import pyaudio 
import vosk
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
from llama_cpp import Llama

load_dotenv()

CHANNELS = 1
FRAME_RATE = 16000
DURATION = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
MODEL_PATH = "/home/arthur/dev/python-projects/english-for-newbies/model/vosk-model-en-us-0.22/vosk-model-en-us-0.22"
API_KEY = os.getenv("OPENAI_API_KEY")


model = vosk.Model(MODEL_PATH)
r = vosk.KaldiRecognizer(model, FRAME_RATE)
llm = Llama() #TODO: implement llama


def get_user_audio(chunk=1024):
    p = pyaudio.PyAudio()
    stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, input_device_index=1, frames_per_buffer=chunk)
    print("I'm listening...")

    try:
        text = ""
        while True:
            data = stream.read(chunk)

            if r.AcceptWaveform(data):
                result = r.Result()
                text = json.loads(result)["text"]
                # cased = subprocess.check_output("python recasepunc/recasepunc.py predict recasepunc/checkpoint", text=True, input=text)
                print(text)
                return text
                
    except KeyboardInterrupt:
        print("Stream terminated.")

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

def get_model_answer(user_input):
    #TODO: add logic
    pass

def initiate_conversation():
    while True:
        speech = get_user_audio()

        answer = get_model_answer(speech)
        print(answer)

initiate_conversation()