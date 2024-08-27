#Beenana02#

#script is meant to reset the jukebox script#
import RPi.GPIO as GPIO
from gpiozero import Button
import time
import os, signal
import subprocess
resetB= Button(23, bounce_time=1)
scriptOn= False
def onOff():
    global subprocess
    extProc = subprocess.Popen(['python','/home/gabi/FinalRFID/RFIDPlayerAndScanner.py'])
    global scriptOn
    
    if scriptOn == True:
        print('off')
        subprocess.Popen.terminate(extProc)
        scriptOn = False
    else:
        subprocess.Popen('python /home/gabi/FinalRFID/RFIDPlayerAndScanner.py',shell=True, preexec_fn=os.setsid)
        scriptOn = True

while True:
    try:
        resetB.when_pressed = onOff
    except KeyboardInterrupt:
        GPIO.cleanup() 
