class Ship:
    """ This class is intended to represent the ship the player controls in the game. For now,
    we won't worry about anything but getting the movement right. So, the attributes are:
    :position: the position vector. A list of two components, each one an int: x, y
    :velocity: the velocity vector. A list of two components, each one an int: x, y
    :direction: the input direction vector. A list of two components, each one an int: x, y.
    The idea is that its coordinates are mapped to the eight cardinal directions
    :f_counter: a frame counter responsible for simulating acceleration frame by frame """
    def __init__(self):
        self.position = [0,0]
        self.velocity = [0,0]
        self.direction = [0,0]
        self.f_counter = [0,0]

    def move(self, delta: float, input: list[bool]):
        """ moves the spaceship by adding to its position the velocity at the given frame, multiplied by delta """
        self.__calculate_velocity(input)
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i] * delta

    def __calculate_velocity(self, input: list[bool]):
        """ recalculates the velocity vector by adding to each component the input direction multiplied by the
        frame counter"""
        self.__calculate_new_direction(input)
        for i in range(len(self.velocity)):
            self.velocity[i] += self.direction[i] * self.f_counter[i]

    def __calculate_new_direction(self, input: list[bool]):
        """ Gets a new direction for the spaceship, done in such a wat that if two opposite keys are pressed at the
        same time, left and up get priority. Maybe it could be done by adding so that if two exactly opposite inputs
        are touched the spaceship just stops accelerating altogether
         :param input: the input the user is giving. 4 bools: left,right,up,down """
        output = [0,0]
        if input[0]: # left
            output[0] += 1
        elif input[1]: # right
            output[0] -= 1
        if input[2]: # up
            output[1] -= 1
        elif input[3]: # down
            output[1] += 1
        self.__get_f_counter(output)
        self.direction = output

    def __get_f_counter(self, new_direction: list[int]):
        """ Given an input list of two integers between -1 and 1, compares said list to direction,
        then updates f_counter accordingly """
        for i in range(len(new_direction)):
            if new_direction[i] != self.direction:
                self.f_counter[i] = 0
            else:
                self.f_counter[i] += 1