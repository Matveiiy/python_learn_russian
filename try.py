import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Задать голос по умолчанию
engine.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Aleksandr':
        engine.setProperty('voice', voice.id)

engine.say("Привет")
engine.say("комплимент")
engine.runAndWait()