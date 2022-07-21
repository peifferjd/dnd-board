import board
import neopixel
import numpy as np
from time import sleep

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
        """Creates an array that maps the position in the array (basically x,y of the gamebaord) to a pixel location along the strip. The roll occus because the first row only has 9 LEDs"""
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
        """Sets brightness of every LED. Not sure if you can set individual ones?"""
        if brightness > 1.0 or brightness < 0:
            return 0
        self._pixels.brightness = brightness
        return 1

    def fillRow(self,row:int, color: tuple[int]):
        """Fills an entire row of the board with a color and displays it"""
        for i in self._dndboard[row,:]:
            self._pixels[i] = color
        self._pixels.show()

    def fillBoard(self,arr: np.ndarray):
        """Pass an array of the shape of the gameboard and it will fill that shape. Array must be row x col x 3"""
        if arr.shape[0] != self._nrows or arr.shape[1] != self._ncols or arr.shape[2] != 3:
            print("Wrong array dimensions.")
            return
        arr[arr > 255] = 255
        arr[arr < 0] = 0
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                self._pixels[self._dndboard[i,j]] = arr[i,j,:]
        self._pixels.show()

    def fill(self, color: tuple[int]):
        """Fills the whole board with a single color"""
        self._pixels.fill(color)

    def fillZero(self):
        """If no arguments are passed, just set the board to zero"""
        self._pixels.fill((0,0,0))
        self._pixels.show()

    def modulateFill(self,arr: np.ndarray):
        """Stores the array you give, and randomly moves a few ints off that color code to create a cool effect."""
        original_board = arr
        for _ in range(1):
            stepped = original_board
            randarr = np.random.randint(-5,5,(10,10,3))
            for _ in range(15):
                stepped += randarr
                #stepped[stepped > 255] = 255 
                #stepped[stepped < 0] = 0
                self.fillBoard(stepped)
                sleep(0.1)
            for _ in range(15):
                stepped -= randarr
                #stepped[stepped > 255] = 255 
                #stepped[stepped < 0] = 0
                self.fillBoard(stepped)
                sleep(0.1)

