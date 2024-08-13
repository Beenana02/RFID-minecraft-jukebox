#--Beenana02--#

#start up script for RFID jukebox. 

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)


#splash screen set up
disp.begin()
disp.clear()
disp.display()
print('test')
splashScreen=Image.open('splashscreen.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

disp.image(splashScreen)
print('pass')
disp.display()

