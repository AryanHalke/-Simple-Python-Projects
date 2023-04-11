import requests
import json
import pyttsx3

city = input("Enter the name of the city : ")
url = f"https://api.weatherapi.com/v1/current.json?key=86322b064639405985a134523230704&q={city}"

r = requests.get(url)
# print(r.text)
print("***Temperature is in Fahrenheit*** ")
wdic = json.loads(r.text)
w = wdic["current"]["temp_f"]
print(w)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(say):
    engine.say(say)
    engine.runAndWait()


say = f"the current weather at {city} is {w} degrees fahrenheit"
speak(say)
