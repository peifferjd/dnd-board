import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18,300,brightness=0.5)
pixels.fill((0,255,0))
time.sleep(5)
pixels.fill((0,0,0))
