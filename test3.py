from Dndboard import Dndboard
import numpy as np

board = Dndboard()
board.setBrightness(0.5)
f='go'
while f != 'stop':
    randarr = np.random.randint(0,255,(10,10,3))
    board.fillBoard(randarr)
    f = input('stop to stop')