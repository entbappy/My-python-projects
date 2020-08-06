#Healthy programmer
# 9am - 5pm
# Water = water.mp3 (3.5 liters)every 40min - Drank - log
# Eyes = eyes.mp3 (Every 30 min) - EyesDone - log
# Pysical Activity = pysical.mp3 (every 45 min)- ExDone - log
#
# Rules - pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")



if __name__ == '__main__':

    init_waters = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10  #40min
    eyessecs = 30  #30 min
    exsecs = 50    #45 min

    while True:
        if time() - init_waters > watersecs:
            print ("Drink Water!! ..Write 'drank' to stop the alarm")
            musiconloop('waters.mp3' ,'drank')
            init_waters = time()
            log_now("Drank water at")

        if time() - init_eyes > eyessecs:
            print ("Eyes Exercise time!! ..Write 'doneeyes' to stop the alarm")
            musiconloop('eyes.mp3' ,'doneeyes')
            init_eyes = time()
            log_now("Eyes relaxed done at")

        if time() - init_exercise > exsecs:
            print ("Exercise Time!! ..Write 'doneex' to stop the alarm")
            musiconloop('excercise.mp3' ,'doneex')
            init_exercise = time()
            log_now("Exercise done at")
