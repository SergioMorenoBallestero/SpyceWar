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
        self.update_acceleration(keyboard)
        self.update_velocity()
        self.position += self.velocity

    def update_velocity(self):
        """ Updates the velocity by adding the value of acceleration
         **This function must do a check to ensure the cap acceleration isn't reached**"""
        # this feels weird... I should check it later prolly
        if (self.velocity + self.acceleration).length() <= constants.VELOCITY_CAP:
            self.velocity += self.acceleration

    def update_acceleration(self, keyboard: list[int]):
        """ Updates the acceleration value by comparing the input to the velocity """
        # what if the input is null?
        if keyboard == [0,0]:
            if self.velocity.x != 0 or self.velocity.y != 0:
                # assign an acceleration opposite to velocity to slow the ship down
                # the vector will be normalized either way, we can assign the values directly
                self.acceleration.x, self.acceleration.y = self.velocity.x, self.velocity.y
                self.acceleration.scale(-1)
        else:
            # assign the input values to acceleration
            self.acceleration.x, self.acceleration.y = keyboard[0], keyboard[1]
        # normalize the acceleration vector
        self.acceleration.normalize()
        # scale the acceleration vector
        self.acceleration.scale(constants.ACCELERATION)