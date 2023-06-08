import eel
import voice_msg
import generate_answer

eel.init("web")

max_length: int = 10
repetition_penalty: float = 5.0
top_k: int = 10
top_p: float = 0.95
temperature: float = 1


@eel.expose
def send_message(msg):
    answer = generate_answer.generate_simple_answer(msg, max_length, repetition_penalty, top_k, top_p, temperature)
    return answer

@eel.expose
def send_voice_message():
    msg = voice_msg.start_recognition()
    answer = generate_answer.generate_simple_answer(msg, max_length, repetition_penalty, top_k, top_p, temperature)
    return answer

@eel.expose
def msg_reader(answer):
    voice_msg.play_audio(answer)
    pass

@eel.expose
def max_length_change(value):
    global max_length
    max_length = int(value)
    print(type(max_length),max_length)
    pass

@eel.expose
def repetition_penalty_change(value):
    global repetition_penalty
    repetition_penalty = float(value)
    print(type(repetition_penalty), repetition_penalty)
    pass

@eel.expose
def top_k_change(value):
    global top_k
    top_k = int(value)
    print(type(top_k),top_k)
    pass

@eel.expose
def top_p_change(value):
    global top_p
    top_p = float(value)
    print(type(top_p), top_p)
    pass

@eel.expose
def temperature_change(value):
    global temperature
    temperature = float(value)
    print(type(temperature), temperature)
    pass

eel.start("desktop.html", size=(1280, 720))