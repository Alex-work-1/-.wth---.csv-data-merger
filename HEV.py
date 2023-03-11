import pyttsx3


# Voice module

class HEV:
    def __init__(self, voiceNumber = 0, rate = 175):
        self.engine = pyttsx3.init()

        self.voices = self.engine.getProperty('voices')

        self.engine.setProperty('voice', self.voices[voiceNumber].id)

        self.engine.setProperty('rate', rate)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


