# main.py -- put your code here!
# Color LED Panel for cocaenTW
# MIT License; © 2023 ArchTW
import neopixel
import machine
import time
import random

# ESP32 Control Pin Number
ESP32_PIN = 13

# LED strip count
LED_CNT= 64

# TEST_MODE =  0 or 1
TEST_MODE = 0

# LED strip connected to ESP32 Pin 13.
n = neopixel.NeoPixel(machine.Pin(ESP32_PIN), LED_CNT, bpp=3)

v = 0
while True:
    if TEST_MODE == 0:
        v %= 2
        for i in range(LED_CNT):
            if (i+v) % 2 == 0:
                n[i] = (255, 0, 0)
            else:
                n[i] = (0, 255, 0)
    else:
        if v == 0:
            n[LED_CNT-1] = (0, 0, 0)
        else:
            n[v-1] = (0, 0, 0)
        r = random.randrange(LED_CNT)
        g = random.randrange(LED_CNT)
        b = random.randrange(LED_CNT)
        n[v] = (r, g, b)
        v %= LED_CNT
    
    v += 1
    # Update the strip.
    n.write()
    time.sleep(0.01)