import math

class Vector3:
    """Represents a three dimensional value of some description."""
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        """Gives you the distance from (0, 0, 0) to the location specified by this vector."""
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def dot(self, other):
        """Gives you the dot product of this and another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def unit(self):
        """Gives a version of this vector where the length is 1."""
        return self / self.length()

    def __add__(self, other):
        if isinstance(other, Vector3): return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else: return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector3): return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        else: return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vector3): return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else: return Vector3(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        if isinstance(other, Vector3): return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        else: return Vector3(self.x / other, self.y / other, self.z / other)
