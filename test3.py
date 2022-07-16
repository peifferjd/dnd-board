from Dndboard import Dndboard
import numpy as np
from time import sleep

board = Dndboard()
board.setBrightness(0.5)
for _ in range(100):
    randarr = np.random.randint(0,255,(10,10,3))
    board.fillBoard(randarr)
    sleep(0.1)
board.fillZero()
