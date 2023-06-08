import speech_recognition
import gtts
from playsound import playsound
import os
import pyttsx3

def record_and_recognize_audio(*args: tuple):
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)
        except speech_recognition.WaitTimeoutError:
            print("Can you check your microphone, please?")
            return
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Check your internet connection, please")
        return recognized_data


# воспроизведение звука из создающегося файла
def play_audio_from_mp3(user_phrase):
    tts = gtts.gTTS(user_phrase, lang="ru")
    tts.save("user_phrase.mp3")
    playsound("user_phrase.mp3")
    os.remove("user_phrase.mp3")
    pass


# воспроизведение указанного звука
def play_audio(user_phrase):
    # не работает write_to_fp
    # mp3_fp = BytesIO()
    # tts = gtts.gTTS('hello', lang='en')
    # tts.write_to_fp(mp3_fp)
    engine = pyttsx3.init()
    engine.say(user_phrase)
    engine.runAndWait()
    pass


# главная функция приложения
def start_recognition():
    key = True
    #recognizer = speech_recognition.Recognizer()
    #microphone = speech_recognition.Microphone()
    voice_input = ""

    while key == True:
        voice_input = record_and_recognize_audio()
        print(voice_input)
        #play_audio_from_mp3(voice_input)
        play_audio(voice_input)
        key = False

    return voice_input