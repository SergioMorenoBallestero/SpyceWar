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
        if keyboard[0] == 0 or keyboard[0] == 0: # if there is some null input value
            if keyboard[0] == 0 and self.velocity.x != 0: # case 1: x input is 0, and x velocity is not 0
                self.acceleration.x = self.velocity.x
            if keyboard[1] == 0 and self.velocity.y != 0: # case 2: y input is 0, and y velocity is not 0
                self.acceleration.y = self.velocity.y
            self.acceleration.scale(-1)
        else:
            # just assign the input values to acceleration
            self.acceleration.x, self.acceleration.y = keyboard[0], keyboard[1]
        # normalize the acceleration vector
        self.acceleration.normalize()
        # adjust the acceleration scale
        self.__update_accel_scale()


    def __update_accel_scale(self):
        """ Scales the acceleration depending on the velocity cap """
        # check whether the new velocity will be greater than the current one
        if self.velocity.length != constants.VELOCITY_CAP:
            # scale the acceleration vector
            self.acceleration.scale(constants.ACCELERATION)
            if (self.velocity + self.acceleration).length() > constants.VELOCITY_CAP:
                # the scale of the acceleration should be the difference between the cap and the current velocity
                difference = constants.VELOCITY_CAP - self.velocity.length()
                self.acceleration.scale(difference / constants.ACCELERATION)


    def __update_velocity(self):
        """ Updates the velocity by adding the value of acceleration, or forcing it to its max value """
        # the first if statement is there to maintain acceleration and preserving direction changes
        if self.velocity.length() == constants.VELOCITY_CAP: # special case: velocity is already at its max value
            # set the velocity to the normalized acceleration (if this triggered, acceleration has not been scaled)
            self.velocity = Vector2(self.acceleration.x,self.acceleration.y)
            # scale it to its maximum value
            self.velocity.scale(constants.VELOCITY_CAP)
        else:
            self.velocity += constants.ACCELERATION