import pyaudio 
 # mic = index 1

CHANNELS = 1
FRAME_RATE = 16000
DURATION = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

def record_mic(chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, input_device_index=1, frames_per_buffer=chunk)
    print("I'm listening...")
    frames = []
    for _ in range(0, int(FRAME_RATE * DURATION / chunk)):
        data = stream.read(chunk)
        frames.append(data)
    print("Good talking!")

def transcribe_audio():
    pass