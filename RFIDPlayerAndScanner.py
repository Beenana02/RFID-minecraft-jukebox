#RFID Scanner

#-Beenana02

from mfrc522 import SimpleMFRC522
import pygame
from time import sleep
from gpiozero import Button, RotaryEncoder
pygame.mixer.init()
#plan to add an lcd screen in later
#from rpi_lcd import LCD

#CHANGE THIS TO YOUR FOLDER WITH MUSIC#
path = "/home/gabi/FinalRFID/music/"

#List of RFID card ids
music_list = [907369626972,390225684907,429139686602]
reader=SimpleMFRC522()

#button control
paused=False
button=Button(22)
def pausing1():
    global paused
    if paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    paused = not paused
    print(paused)
def test():
    print("hi")
#mute=Button(16)
#will add volume and reset buttons/slider in the future
#volume
volumeRotary = RotaryEncoder(18,17)
vol= 1
pygame.mixer.music.set_volume(vol)
def volumeCon():
    global vol
    vol += 0.2
    pygame.mixer.music.set_volume(vol)
    print(pygame.mixer.music.get_volume())
def volumeConNega():
    global vol
    vol -= 0.2
    pygame.mixer.music.set_volume(vol)
    print(pygame.mixer.music.get_volume())
muteB= Button(27)
muted = False
def muted():
    global muted
    if muted:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(vol)
    muted = not muted
    

#Shows what songs is currently playing to prevent a double reading 
currentSong=0

bluetoothC=False
auxC=False

def safe_exit(signum, frame):
    exit(1)
 
try:
    button.when_pressed = pausing1
    muteB.when_pressed = muted
    sleep(0.2)
    volumeRotary.when_rotated_clockwise = volumeCon
    volumeRotary.when_rotated_counter_clockwise = volumeConNega
    
     
    #loops over song list as long as bluetooth and audio jack aren't being used 
    while (bluetoothC or auxC ==False):

        print("Waiting for record scan...")
        id= reader.read()[0]
        print("Card Value is:",id) 
        if id in music_list:
            if(id == currentSong) and (pygame.mixer.music.get_busy()):
                print('song is already playing')
            elif(paused==False):
                if (id==907369626972):
                    
                    # playing a song
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
                    pygame.mixer.music.load(path + "pigstep.mp3")
                    print('pigstep')
                    currentSong=429139686602
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
                elif (id==1046718834915):
                    import pygame
                    pygame.mixer.init()
                    pygame.mixer.music.load(path + "Wait.mp4")
                    print('wait')
                    currentSong=1046718834915
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()

        else:
            print('not readable disc')
            print('playing the default mineraft soundtrack')
            pygame.mixer.init()
            pygame.mixer.music.load(path + "alpha.mp3")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            currentSong=None

finally:
    pass
