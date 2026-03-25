class Vector2:
    """ This class is intended to be a basic implementation of vectors for everything movement
    related in the game
    """
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def length(self) -> float:
        """ returns the length of the vector """
        return (self.x**2 + self.y**2)**0.5

    def normalize(self):
        """ normalizes the vector """
        length = self.length()
        self.x /= length
        self.y /= length

    def scale(self, num: float = 1):
        """ scales the vector by a factor of num """
        self.x *= num
        self.y *= num

    def __add__(self,other: Vector2) -> Vector2:
        """ basic implementation of a sum of two vectors """
        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x + other.x, self.y + other.y)