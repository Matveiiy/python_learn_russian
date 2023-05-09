import copy
from time import sleep
import os
import random

#from gtts import gTTS
#from pydub import AudioSegment
#from pydub.playback import play
#import subprocess
#from playsound import playsound
#import winsound
#import asyncio
  
'''
def say_text(text):
    obj1 = gTTS(text = text, lang = "ru", slow = False)
    obj1.save("word.mp3")
    
    #subprocess.run("start " + os.getcwd().)
    
    #song = AudioSegment.from_mp3("word.mp3")
    #play(song)

    #os.system("start " + os.getcwd().replace("\\", "/") + "/word.mp3")
    #sleep(3)
    

    #winsound.PlaySound('word.wav')
    
    #playsound("word.mp3")
'''

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru') 

# Задать голос по умолчанию

# Попробовать установить предпочтительный голос
'''
for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft Irina Desktop - Russian':
        engine.setProperty('voice', voice.id)
'''
def say_text(text):
    engine.say(text)
    engine.runAndWait()



def mainloop():
    words = []
    print("Программа берёт данные из файла all.txt, в used.txt хранятся использованные слова без ошибок")
    print("Комманды:")
    print("выход -- выйти")
    print("повтори -- повторить слово")
    print("сколько -- сказать, сколько слов уже использовано")
    original_words = []
    try:
            
        with open("all.txt", encoding='utf-8', mode = "r") as file:
            for line in file:
                s = line.strip('\n').strip(' ')
                if not s: continue
                original_words.append(s)
    except:
        print("ERROR: Неу далось открыть файл all.txt")
        return
    say_text("Привет")
    run = True
    used_file = -1
    words = []
    try:
        used_words = set();newwords = []
        with open("used.txt", encoding='utf-8', mode = "r") as f:
            for line in f:
                s = line.strip('\n').strip().lower()
                used_words.add(s)
        for i in original_words:
            if not (i in used_words): newwords.append(i)
        for word in newwords:
            words.append(word)
    except:
        words = copy.deepcopy(original_words)
    used_file = open("used.txt", encoding = 'utf-8', mode = "a")
    random.shuffle(words)
    cnt = -1
    while True:
        cnt+=1
        if cnt == len(words):
            say_text("А слова закончились, начинаем сначала")
            used_file.close()
            used_file = open("used.txt", encoding = 'utf-8', mode = 'w')
            words = copy.deepcopy(original_words)
            random.shuffle(words)
            cnt = -1
            continue
        say_text(words[cnt])
        s = ""
        while True:
            s = input().strip()
            if s == "повтори":
                say_text(words[cnt])
                continue
            if s == "сколько":
                say_text("Использованно " + str(len(original_words) - len(words) + cnt) + " слова")
                continue
            break
        #print(s)
        #print(words[cnt])
        #print(len(s), len(words[cnt]))
        #print(ord(words[cnt][len(words[cnt]) - 1]))
        if s == "выход":
            say_text("Пока")
            break
        if s == words[cnt]:
            say_text("Молодец")
            used_file.write(words[cnt] + '\n')
        else:
            say_text("Чуть-чуть не так")
            print(words[cnt])
    used_file.close()

mainloop()