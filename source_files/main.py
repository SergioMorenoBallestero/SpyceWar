import pyxel
import constants
from board import Board


board = Board()
pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, title="SpyceWar", fps=60)
pyxel.load("assets.pyxres")
pyxel.run(board.update, board.draw)