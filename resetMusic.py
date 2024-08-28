#Beenana02#

#script is meant to startup before the jukebox script#
import RPi.GPIO as GPIO
from gpiozero import Button
import time
import os, signal
import subprocess
from demo_opts import get_device
from luma.core.render import canvas
from luma.core.virtual import viewport

def scroll_message(speed=5):
    x = device.width

    # First measure the text size
    with canvas(device) as draw:
        left, top, right, bottom = draw.textbbox((0, 0), 'Press the button to start the jukebox https://github.com/Beenana02/RFID-minecraft-jukebox')
        w, h = right - left, bottom - top

    virtual = viewport(device, width=max(w, 1000), height=max(h, 100))
    with canvas(virtual) as draw:
        draw.text((x, device.height - 12), 'Press the button to start the jukebox https://github.com/Beenana02/RFID-minecraft-jukebox', fill="white")
    i = 0
    while i < x + w:
        virtual.set_position((i, 0))
        i += speed
        time.sleep(0.025)


resetB= Button(23, bounce_time=4)
scriptOn= False
def onOff():
    global subprocess
    global scriptOn
    
    if(scriptOn == True):
        print('off')
        subprocess.Popen.terminate('python /home/gabi/FinalRFID/RFIDPlayerAndScanner.py')
        scriptOn = False
    elif(scriptOn == False):
        subprocess.Popen('python /home/gabi/FinalRFID/RFIDPlayerAndScanner.py',shell=True)
        scriptOn = True

while True:
    resetB.when_pressed = onOff
    if __name__ == "__main__":
        try:
            device = get_device()
            if(scriptOn ==False):
                scroll_message()
            elif(scriptOn ==True):
                device.clear()
        except KeyboardInterrupt:
            GPIO.cleanup()
