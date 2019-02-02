from Material import *
from Vector3 import *
from Ray import *
from Bounce import *

class Metal(Material):
    """Shiny metal material hell yeah."""

    def __init__(self, attenuation):
        self.attenuation = attenuation

    def scatter(self, strike):
        """
        See Material.
        basically just bounces some rays around smoothly and modulates.
        """
        reflected = strike.ray.direction.unit().reflect(strike.normal)
        scattered = Ray(strike.point(), reflected)
        if (scattered.direction.dot(strike.normal) > 0): return Bounce(self.attenuation, scattered)
        return Bounce(self.attenuation)
