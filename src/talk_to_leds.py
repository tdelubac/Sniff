import sys
import board
import neopixel
import time
import numpy as np


PIX_PIN = board.D18
PIX_NUM = 8
pixels = neopixel.NeoPixel(PIX_PIN, PIX_NUM, brightness=0.05, auto_write=False)


def flash(color):
    pixels.fill((0,0,0))
    pixels.show()
    pixels.fill(color)
    pixels.show()
    time.sleep(0.1)
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(0.1)

    
def color_scale(pos):
    pos_min = 20
    pos_max = 80
    pos_med = (pos_max - pos_min)/2. + pos_min
    if pos < pos_min:
        g = b = 0
        r = 255
    elif pos > pos_max:
        r = g = 0
        b = 255
    elif pos < pos_med:
        b = 0
        g = int(255 * (pos - pos_min) / (pos_med - pos_min))
        r = int(255 * (1 - (pos - pos_min) / (pos_med - pos_min)))
    else:
        b = int(255 * (pos - pos_med) / (pos_max - pos_med))
        g = int(255 * (1 - (pos - pos_med) / (pos_max - pos_med)))
        r = 0
    return (r,g,b)
                

def stop_leds():
    pixels.fill((0,0,0))
    pixels.show()


def set_color(power):
    '''Set LEDs color
    '''
    color = color_scale(-power)
    pixels.fill(color)
    pixels.show()

