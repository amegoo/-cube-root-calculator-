import pyttsx3

engine = pyttsx3.init()
talk=input("inter the words you want to listin to:")
engine.say(talk)
engine.runAndWait()
engine.stop()
