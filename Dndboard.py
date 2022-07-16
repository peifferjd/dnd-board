import board
import neopixel
import numpy as np

class Dndboard:
    
    def __init__(self, pixel_count=100, nrows=10, pixel_pin=board.D18) -> None:
        """
        pixel_count: number of LEDs in the strip
        nrows: number of rows of leds
        pixel_pin: GPIO pin connected to the LEDs"""

        self._pixels = neopixel.NeoPixel(pixel_pin,pixel_count,brightness=0.2,auto_write=False)
        self._nrows = nrows
        self._npixel = pixel_count
        self._ncols = int(self._npixel/self._nrows)

        self.__createmapping()

    def __createmapping(self):
        self._dndboard = np.zeros((self._nrows,self._ncols),dtype=int) 
        pixelnums = np.arange(self._npixel)
        pixelnums = np.roll(pixelnums,1)
        pixelnums[0] = 0
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

    def fillBoard(self,arr: np.ndarray):
        """Pass an array of the shape of the gameboard and it will fill that shape"""
        if arr.shape[0] != self._nrows or arr.shape[1] != self._ncols or arr.shape[2] != 3:
            print("Wrong array dimensions.")
            return
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                self._pixels[self._dndboard[i,j]] = arr[i,j,:]
        self._pixels.show()

    def fillZero(self):
        """If no arguments are passed, just set the board to zero"""
        self._pixels.fill((0,0,0))
        self._pixels.show()
