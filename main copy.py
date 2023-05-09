# Import the required module for text 
# to speech conversion
from gtts import gTTS
from playsound import playsound
import json
  
# This module is imported so that we can 
# play the converted audio
import os

def say_text(text):
    obj1 = gTTS(text = text, lang = "ru", slow = False)
    obj1.save("try.mp3")
    playsound(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + "/try.mp3")

words = []
def parse_words(file):
    global words
    for line in file:
        if not line.strip(): continue
        words.append(line[0:-1])
def parse_files(ffrom, fto):
    fto+=1
    for i in range(ffrom, fto):
        with open("data" + str(i) + ".txt", encoding = 'utf-8', mode = "r") as f:
            parse_words(f)
parse_files(1,19)
words.sort()
'''
cnt = 0
curf = open("data_а.txt", encoding= 'utf-8', mode = 'w')
curf.write(words[0] + '\n')
for i in range(1, len(words)):
    if words[i][0] == words[i-1][0]: 
        #print(words[i] + '\n')
        curf.write(words[i] + '\n')
        continue
    curf.close()
    cnt += 1
    curf = open("data_" + chr(cnt + ord('а')) + '.txt', encoding= 'utf-8', mode = 'w')
'''
with open("all.txt", encoding= 'utf-8', mode = "w") as f:
    for i in words:
        f.write(i + '\n')
'''
for i in range(len(words)):
    print(words[i], end = '\n')
'''
