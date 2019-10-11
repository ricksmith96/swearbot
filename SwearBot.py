from playsound import playsound
from gtts import gTTS
import urllib.request
import random
import time
import json
import os

one = ("You are", "Eat my", "Go fuck my", "Lick my", "Batman")
two = ("brown", "blue", "yellow", "black", "white", "poop loving", "lard", "seal")
three = ("asshole", "shit", "ass", "piss", "balls", "butter face")
shit = "mp3.mp3"
#These are word that program will mix to make swears

while 1:
    num0 = random.randrange(0,5)
    num1 = random.randrange(0,8)
    num2 = random.randrange(0,6)
    piss = one[num0] + ' ' + two[num1] + ' ' + three[num2]
    print(piss)
    tts = gTTS(text=piss, lang='en') #This is for prgram to say
    tts.save(shit)
    playsound(shit)
    os.remove(shit)
    pass
