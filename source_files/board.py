import pyxel
import time
from ship import Ship

class Board:
    """ This class represents the game window """
    def __init__(self):
        self.then = 0
        self.player = Ship()


    def parse_input(self) -> list[int]:
        """ gets the input from the keyboard in order to pass it to player.move() """
        output = [0,0]
        if pyxel.btn(pyxel.KEY_A):
            output[0] = -1
        elif pyxel.btn(pyxel.KEY_D):
            output[0] = 1
        if pyxel.btn(pyxel.KEY_S):
            output[1] = 1
        elif pyxel.btn(pyxel.KEY_W):
            output[1] = -1
        return output


    def update(self):
        now = time.time()
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
        self.player.move(self.parse_input())
        print(self.player)
        self.then = time.time()


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.position.x,self.player.position.y,0,0,0,16,16)