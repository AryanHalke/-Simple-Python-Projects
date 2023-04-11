import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(say):
    engine.say(say)
    engine.runAndWait()


while True:
    say = input("Enter text to speech : ")
    speak(say)
