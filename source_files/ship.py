import constants
from vector2 import Vector2

class Ship:
    """ This class is intended to represent the ship the player controls in the game. For now,
    we won't worry about anything but getting the movement right. So, the attributes are:
    :position: the position vector. Vector2 type. Position should NEVER have negative values
    :__velocity: the __velocity vector. Vector2 type.
    :__acceleration: the __acceleration vector. doubles as direction. Vector2 type. """
    def __init__(self):
        self.position = Vector2()
        self.__velocity = Vector2()
        self.__acceleration = Vector2()


    def __update_acceleration(self, keyboard: list[int]):
        """ Updates the __acceleration value by comparing the input to the __velocity """
        # assign the input values to __acceleration
        self.__acceleration.x, self.__acceleration.y = keyboard[0], keyboard[1]
        # an __acceleration contrary to the __velocity should be assigned
        if (keyboard[0] == 0): # case 1: x input is 0
            self.__acceleration.x = self.__velocity.x
            self.__acceleration.x *= -constants.FRICTION_FACTOR

        if (keyboard[1] == 0): # case 2: y input is 0
            self.__acceleration.y = self.__velocity.y
            self.__acceleration.y *= -constants.FRICTION_FACTOR

        if (self.__acceleration.length() != 0): # check just to avoid dividing by 0
            self.__acceleration.normalize()
        self.__update_accel_scale()


    def __update_accel_scale(self):
        """ Scales the __acceleration depending on the __velocity cap """
        new_vel = Vector2(self.__velocity.x + self.__acceleration.x,self.__acceleration.y + self.__acceleration.y)

        if self.__velocity.length() < constants.VELOCITY_CAP:
            self.__acceleration.scale(constants.ACCELERATION)

            if new_vel.length() > constants.VELOCITY_CAP:
                # the scale of the __acceleration should then cover just enough to reach the velocity_cap
                difference = constants.VELOCITY_CAP - self.__velocity.length()
                self.__acceleration.scale(difference / constants.ACCELERATION)


    def __update_velocity(self):
        """ Updates the __velocity by adding the value of __acceleration, or forcing it to its max value """
        # in the default case, increment and assign the __acceleration values to __velocity
        self.__velocity += self.__acceleration

        # clamping velocity to the max value
        if self.__velocity.length() >= constants.VELOCITY_CAP:
            self.__velocity.normalize()
            self.__velocity.scale(constants.VELOCITY_CAP)

        # forcing a stop when too slow
        elif self.__velocity.length() < constants.ACCELERATION - 1:
            self.__velocity.scale(0)


    def move(self, keyboard: list[int], delta_seconds: float):
        """ Updates the position of the ship based on keyboard input. """
        inf_limit = constants.SCREEN_HEIGHT - constants.SPRITE_HEIGHT
        right_limit = constants.SCREEN_WIDTH - constants.SPRITE_WIDTH
        self.__update_acceleration(keyboard)
        self.__update_velocity()

        scaled_vel = Vector2(self.__velocity.x,self.__velocity.y)
        scaled_vel.scale(delta_seconds)
        new_pos = self.position + scaled_vel
        # x bounds checking
        if new_pos.x < 0:
            print("stuck on left")
            print(self)
            self.position.x = 0
            self.__velocity.x = 0
        elif new_pos.x > right_limit:
            print("stuck on right")
            print(self)
            self.position.x = right_limit
            self.__velocity.x = 0
        else:
            self.position.x = new_pos.x

        # y bounds checking
        if new_pos.y < 0:
            print("stuck upwards")
            print(self)
            self.position.y = 0
            self.__velocity.y = 0
        elif new_pos.y > inf_limit:
            print("stuck downwards")
            print(self)
            self.position.y = inf_limit
            self.__velocity.y = 0
        else:
            self.position.y = new_pos.y


    def __str__(self) -> str:
        """ shows the 3 vectors of interest: __velocity, __acceleration, position """
        return "vel: " + str(self.__velocity) + "\n" + "accel: " + str(self.__acceleration) + "\n" + "pos: " + str(self.position)

    # properties and setters
    @property
    def position(self) -> Vector2:
        return self.__position

    @position.setter
    def position(self, position: Vector2):
        if not isinstance(position, Vector2):
            raise TypeError("The position vector is not a vector!")
        elif (position.x < 0 or position.x > constants.SCREEN_WIDTH + constants.SPRITE_WIDTH or position.y < 0 or
              position.y > constants.SCREEN_HEIGHT + constants.SPRITE_HEIGHT):
            raise ValueError("The position went out of bounds!")
        else:
            self.__position = position