#--Beenana02--#

#start up script for RFID jukebox. 
#currently WIP#
from demo_opts import get_device
from luma.core.render import canvas
from luma.core.virtual import viewport
import time

def scroll_message(speed=5):
    x = device.width

    # First measure the text size
    with canvas(device) as draw:
        left, top, right, bottom = draw.textbbox((0, 0), 'https://github.com/Beenana02/RFID-minecraft-jukebox')
        w, h = right - left, bottom - top

    virtual = viewport(device, width=max(w, 1000), height=max(h, 100))
    with canvas(virtual) as draw:
        draw.text((x, device.height - 12), 'https://github.com/Beenana02/RFID-minecraft-jukebox', fill="white")
        draw.text((x-w, device.height - 30), 'https://github.com/Beenana02/RFID-minecraft-jukebox', fill="white")
    virtual2 = viewport(device, width=max(w, 1000), height=max(h, 100))
    with canvas(virtual2) as draw:
        draw.text((x-w, device.height - 30), 'https://github.com/Beenana02/RFID-minecraft-jukebox', fill="white")
    i = 0
    while i < x + w:
        virtual.set_position((i, 0))
        i += speed
        time.sleep(0.025)

#Runs the screen#
def main():
    device = get_device()

    print("Testing basic canvas graphics...")
    while True:
        scroll_message()
if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

