from Material import *
from Vector3 import *
from Ray import *
from Bounce import *

class Metal(Material):
    """Shiny metal material hell yeah."""

    def __init__(self, texture):
        self.texture = texture

    def scatter(self, strike):
        """
        See Material.
        basically just bounces some rays around smoothly and modulates.
        """
        reflected = strike.ray.direction.unit().reflect(strike.normal)
        scattered = Ray(strike.point(), reflected)
        if (scattered.direction.dot(strike.normal) > 0): return Bounce(self.texture.value(0, 0, strike.point()), scattered)
        return Bounce(self.texture.value(0, 0, strike.point()))
