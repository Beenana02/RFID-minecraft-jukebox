#RFID Scanner
#-Beenana02
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import pygame
from gpiozero import Button
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
path = "/home/gabi/FinalRFID/music/"
#List of RFID card ids
music_list = [907369626972,390225684907,429139686602]
reader=SimpleMFRC522()

#button control
paused=False
pause=Button(4)
#mute=Button(16)
#will add volume and reset buttons/slider in the future

#Shows what songs is currently playing to prevent a double reading 
currentSong=0

bluetoothC=False
auxC=False

def safe_exit(signum, frame):
    exit(1)
 
#pause button function
def pauseB(b):
    if b.is_pressed:
        print("pressed")
        if(paused==False):
            paused=True
            pygame.mixer.pause()
        else:
            paused=False
            pygame.mixer.unpause()
 
#loops over song list as long as bluetooth and audio jack aren't bein used 
while (bluetoothC or auxC ==False):
    
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)

        while True:
                print("Waiting for record scan...")
                id= reader.read()[0]
                print("Card Value is:",id)
                pauseB(pause) 
                if id in music_list:
                    if(id == currentSong) and (pygame.mixer.music.get_busy()):
                        print('hi')
                    else:
                        if (id==907369626972):
                            
                            # playing a song
                            import pygame
                            pygame.mixer.init()
                            pygame.mixer.music.load(path + "Ward.mp3")
                            pygame.mixer.music.set_volume(1.0)
                            pygame.mixer.music.play()
                            currentSong=907369626972            
                        elif (id==390225684907):
                        
                            pygame.mixer.init()
                            pygame.mixer.music.load(path + "Stal.mp3")
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
                            currentSong=1046718834915
                            pygame.mixer.music.set_volume(1.0)
                            pygame.mixer.music.play()

                else:
                    print('not readable disc')
                    pygame.mixer.init()
                    pygame.mixer.music.load(path + "alpha.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
                    currentSong=None
   

    finally:
        GPIO.cleanup()