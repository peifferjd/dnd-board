import board
import neopixel
import numpy as np

class Dndboard:
    
    def __init__(self, pixel_count=100, nrows=10, pixel_pin=board.D18) -> None:
        """
        pixel_count: number of LEDs in the strip
        nrows: number of rows of leds
        pixel_pin: GPIO pin connected to the LEDs"""

        self._pixels = neopixel.NeoPixel(pixel_pin,pixel_count,brightness=0.2)
        self._nrows = nrows
        self._npixel = pixel_count
        self._ncols = int(self._npixel/self._nrows)

        self.__createmapping()
        a=5

    def __createmapping(self):
        self._dndboard = np.empty(self._nrows,self._ncols,dtype=int) 
        pixelnums = np.arange(self._npixel)
        for i in range(self._nrows):
            if i % 2 == 0:
                row = pixelnums[i*self._ncols : (i+1)*self._ncols]
            else:
                row = pixelnums[ (i+1)*self._ncols -1 : i*self._ncols -1 : -1]
            self._dndboard[i,:] = row

    def setBrightness(self,brightness: float) -> int:
        if brightness > 1.0 or brightness < 0:
            return 0
        self._pixels.brightness = brightness
        return 1

    def fillRow(self,row:int, color: tuple[int]):
        for i in self._dndboard[row,:]:
            self._pixels[i] = color

