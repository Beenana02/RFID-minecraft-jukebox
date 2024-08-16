#Beenana02#

#script is meant to reset the jukebox script#
from gpiozero import Button
import time
import os, signal
import subprocess

resetB= Button(23, bounce_time=1)
scriptOn= True
def onOff():
    if scriptOn == True:
        os.killpg('/home/gabi/FinalRFID/RFIDPlayerAndScanner.py'.pid, signal.SIGTERM)
    else:
        subprocess.run('/home/gabi/FinalRFID/RFIDPlayerAndScanner.py')

while True:
    resetB.when_pressed = onOff