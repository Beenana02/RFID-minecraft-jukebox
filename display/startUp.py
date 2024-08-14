#--Beenana02--#

#start up script for RFID jukebox. 
#currently not working#


from pathlib import Path
from demo_opts import get_device
from PIL import Image

splashScreen = Image.open("/home/gabi/FinalRFID/splashscreen.png")
#device.display(splashScreen)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

