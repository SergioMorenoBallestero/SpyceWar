import pyxel
import constants
from board import Board


board = Board()
pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, title="SpyceWar", fps=constants.FPS)
pyxel.load("assets.pyxres")
pyxel.run(board.update, board.draw)