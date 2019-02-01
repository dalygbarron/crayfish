from Vector3 import *

class Ray:
    """Represents a line through 3D space."""
    def __init__(self, origin = Vector3(), direction = Vector3()):
        self.origin = origin
        self.direction = direction

    def point(self, t):
        """Gives a point along the ray at t units. Units are defined by the length of direction."""
        return self.origin + self.direction * t
