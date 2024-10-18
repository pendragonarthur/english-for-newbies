import os
from gtts import gTTS
import openai
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
recognizer = sr.Recognizer()

def generate_bot_answer(user_input): # estou nomeando a variavel como user_input porque nao necessariamente é uma pergunta, mas sim, uma entrada de fala
    answer = openai.completions.create(model = "gpt-3.5-turbo-instruct", messages=[{"role": "user", "content": user_input}])
    return answer.choices[0].message["content"]

def get_user_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def recognize_user_speech(audio):
    try: 
        text = recognizer.recognize_whisper(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Não entendi o que você falou.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return ""
    
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("answer.mp3")
    os.system("start resposta.mp3")

def initiate_talking():
    while True:
        audio = get_user_audio()
        speech = recognize_user_speech(audio)

        if speech.lower == "sair":
            print("Goodbye, bom conversar com você. Até a proxima!")
            break

        answer = generate_bot_answer(speech)
        print(f"Chat: {answer}")
        speak(answer)

initiate_talking()