#RFID Jukebox

#-Beenana02-#
from mfrc522 import SimpleMFRC522
import pygame
from time import sleep
from gpiozero import Button, RotaryEncoder
from subprocess import check_call
import time
from demo_opts import get_device
from luma.core.render import canvas
import RPi.GPIO as GPIO

pygame.mixer.init()
currentSong=0
menuText = ' '

GPIO.setwarnings(False)
device = get_device()
#CHANGE THIS TO YOUR FOLDER WITH MUSIC#

path = "/home/gabi/FinalRFID/music/"

pygame.mixer.music.load(path + "Ward.mp3")
pygame.mixer.music.play()
#List of RFID card ids
music_list = [907369626972,390225684907,429139686602]
reader=SimpleMFRC522()

#button control center
paused=False
button=Button(22)
def pausing1():
    global paused
    if paused:
        pygame.mixer.music.pause()
        menuText = 'PAUSED'
    else:
        pygame.mixer.music.unpause()
        menuText = ' '
    paused = not paused
    updateOLED(device,menuText)
    print(paused)

volumeRotary = RotaryEncoder(18,17)
vol= 1
pygame.mixer.music.set_volume(vol)
def volumeCon():
    global vol
    if vol <1:
        vol += 0.1
        pygame.mixer.music.set_volume(vol)
        updateOLED(device,menuText)
def volumeConNega():
    global vol
    if vol >0.1:
        vol -= 0.1
        pygame.mixer.music.set_volume(vol)
        updateOLED(device,menuText)

muteB= Button(27)
muted = False
def muted():
    global muted
    if muted:
        pygame.mixer.music.set_volume(0)
        menuText = 'MUTED'
    else:
        pygame.mixer.music.set_volume(vol)
        menuText = ' '
    muted = not muted
    updateOLED(device,menuText)
def buttonController():
    if pygame.mixer.music.get_busy():
        button.when_pressed = pausing1
        muteB.when_pressed = muted
        volumeRotary.when_rotated_clockwise = volumeCon
        volumeRotary.when_rotated_counter_clockwise = volumeConNega    
        
#Shows what songs is currently playing to prevent a double reading 
currentSong=0

bluetoothC=False
auxC=False

#lcd WIP

padding = 2

def getTextSize(text):
    with canvas(device) as draw:
        left, top, right, bottom = draw.textbbox((0, 0), text)
        w, h = right - left, bottom - top
    return w, h
def updateOLED(device,menuText):
    x=device.width
    y=device.height
    with canvas(device) as draw:
        text='Minecraft RFID Jukebox'
        draw.text((0, 0+padding),text,fill="white")

        text='Song= '+ str(currentSong)
        w, h = getTextSize(text)
        draw.text(((x/2)-w/2, 20), text, fill="white")

        text='Volume= '+ str(vol*100//1)
        w, h = getTextSize(text)
        draw.text(((x/2)-w/2, 40), text, fill="white")

        w, h = getTextSize(menuText)
        draw.text(((x/2)-w/2, 50), menuText, fill="white")

#def scanDisc():
    
#loops over song list as long as bluetooth and audio jack aren't being used    
while (bluetoothC or auxC ==False): 
    buttonController()
    print("Waiting for record scan...")
    id= reader.read()[0]
    print(id) 
    
    if id in music_list:
        if(id == currentSong) and (pygame.mixer.music.get_busy()):
            print('song is already playing')
        elif(id != currentSong):
            if (id==907369626972):
                pygame.mixer.init()
                pygame.mixer.music.load(path + "Ward.mp3")
                print('ward')
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                currentSong=907369626972
                
            elif (id==390225684907):
                pygame.mixer.init()
                pygame.mixer.music.load(path + "Stal.mp3")
                print('stal')
                currentSong=390225684907
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play()
                
            elif (id==429139686602):
                pygame.mixer.init()
                pygame.mixer.music.load(path + "Pigstep.mp3")
                print('pigstep')
                currentSong=429139686602
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                
            elif (id==1046718834915):
                import pygame
                pygame.mixer.init()
                pygame.mixer.music.load(path + "yo.mp3")
                print('wait')
                currentSong=1046718834915
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()

            else:
                print('not readable disc')
                print('playing the default mineraft soundtrack')
                pygame.mixer.init()
                pygame.mixer.music.load(path + "Cat.mp3")
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                currentSong=None   
    
    updateOLED(device,menuText)
