import constants
from vector2 import Vector2

class Ship:
    """ This class is intended to represent the ship the player controls in the game. For now,
    we won't worry about anything but getting the movement right. So, the attributes are:
    :position: the position vector. Vector2 type. Position should NEVER have negative values
    :velocity: the velocity vector. Vector2 type.
    :acceleration: the acceleration vector. doubles as direction. Vector2 type. """
    def __init__(self):
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()


    def move(self, keyboard: list[int]):
        """ Updates the position of the ship based on keyboard input.
        **This function must do a check to ensure the ship doesn't go OOB**"""
        self.__update_acceleration(keyboard)
        self.__update_velocity()
        self.position += self.velocity


    def __update_acceleration(self, keyboard: list[int]):
        """ Updates the acceleration value by comparing the input to the velocity """
        # assign the input values to acceleration
        self.acceleration.x, self.acceleration.y = keyboard[0], keyboard[1]
        # an acceleration contrary to the velocity should be assigned
        if (keyboard[0] == 0): # case 1: x input is 0
            self.acceleration.x = self.velocity.x
            self.acceleration.x *= -1
        if (keyboard[1] == 0): # case 2: y input is 0
            self.acceleration.y = self.velocity.y
            self.acceleration.y *= -1

        if (self.acceleration.length() != 0): # check just to avoid dividing by 0
            # normalize the acceleration vector
            self.acceleration.normalize()
        # adjust the acceleration scale
        self.__update_accel_scale()


    def __update_accel_scale(self):
        """ Scales the acceleration depending on the velocity cap """
        if (self.velocity.length() < (constants.VELOCITY_CAP - 0.5)): # if velocity isn't already at max
            # scale the acceleration vector
            self.acceleration.scale(constants.ACCELERATION)
            if ((self.velocity + self.acceleration).length() > constants.VELOCITY_CAP): # if new velocity overflows
                # the scale of the acceleration should then cover just enough to reach the velocity_cap
                difference = constants.VELOCITY_CAP - self.velocity.length()
                self.acceleration.scale(difference / constants.ACCELERATION)


    def __update_velocity(self):
        """ Updates the velocity by adding the value of acceleration, or forcing it to its max value """
        # in the default case, increment and assign the acceleration values to velocity
        self.velocity += self.acceleration
        if (self.velocity.length() >= (constants.VELOCITY_CAP - 0.5)): # if velocity is already at max length
            # keep the direction
            self.velocity.normalize()
            # scale it to its maximum value
            self.velocity.scale(constants.VELOCITY_CAP)
        elif (self.velocity.length() < 1): # if it turns out velocity is very small
            # set it to 0 directly
            self.velocity.scale(0)


    def __str__(self) -> str:
        """ shows the 3 vectors of interest: velocity, acceleration, position """
        return "vel: " + str(self.velocity) + "\n" + "accel: " + str(self.acceleration) + "\n" + "pos: " + str(self.position)