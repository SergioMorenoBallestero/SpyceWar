import random
from ship import Ship
from vector2 import Vector2
import constants

class Asteroid:
    """ This class represents an asteroid enemy in the game. It will follow the player around and
    kill him if it touches him, or be destroyed if it goes out of bounds or is shot at by the player.
    They appear out of the screen's bounds, and their acceleration is defined at construction (they
    define a linear trajectory)"""
    def __init__(self,ship):
        self.position = self.__calculate_initial_position(ship)
        self.acceleration = self.__calculate_trajectory(ship)


    def __calculate_initial_position(self, ship: Ship) -> Vector2:
        """ For this class this function will only be called upon creation in the constructor.
        It calculates the initial position the asteroid will have. It should be a random one
        that is out of bounds """
        half_width = constants.SCREEN_WIDTH // 2
        half_height = constants.SCREEN_HEIGHT // 2
        # the x position will be on the opposite half of the screen as the ship's x position
        if ship.position.x <= half_width:
            pos_x = random.randint(half_width,constants.SCREEN_WIDTH)
        else:
            pos_x = random.randint(0,half_width)
        # the y position will be on the opposite half of the screen as the ship's y position
        if ship.position.y >= half_height:
            pos_y = random.randint(half_height,constants.SCREEN_HEIGHT)
        else:
            pos_y = random.randint(0,half_height)

        return Vector2(pos_x,pos_y)


    def __calculate_trajectory(self, ship: Ship) -> Vector2:
        """ For this class this function will only be called upon creation in the constructor.
        It calculates the direction the asteroid will take during its lifetime.
        :param ship: a Ship class object from which we will extract the position """
        if not isinstance(ship, Ship):
            return NotImplemented
        target_pos = ship.position

        return self.position + target_pos.scale(-1)