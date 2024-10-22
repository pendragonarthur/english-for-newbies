import pyaudio 
import vosk
import json
import subprocess

MODEL_PATH = "model/vosk"
model = vosk.Model(MODEL_PATH)

CHANNELS = 1
FRAME_RATE = 16000
DURATION = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

def record_mic(chunk=1024):
    p = pyaudio.PyAudio()
    r = vosk.KaldiRecognizer(model, FRAME_RATE)
    stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, input_device_index=1, frames_per_buffer=chunk)
    print("I'm listening...")
    frames = []

    try:
        while True:
            data = stream.read(chunk)

            if r.AcceptWaveform(data):
                result = r.Result()
                text = json.loads(result)["text"]
                # TODO: baixar recasepunc 
                # cased = subprocess.check_output("python recasepunc/recasepunc.py predict recasepunc/checkpoint", text=True, input=text)
                
            

    except KeyboardInterrupt:
        print("Stream terminated.")
    
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

record_mic()