from Material import *
from Vector3 import *
from Ray import *
from Bounce import *
import random

class Lambert(Material):
    """Lambert material hell yeah."""

    def __init__(self, attenuation):
        self.attenuation = attenuation

    def randomInSphere(self):
        """Gives a random point within a unit sphere. TODO: shitty method"""
        point = Vector3(2, 2, 2)
        while point.squaredLength() > 1: point = Vector3(random.random(), random.random(), random.random()) * 2.0 - 1
        return point

    def scatter(self, strike):
        """
        See Material.
        basically just bounces some rays around randomly looking for more colour, and modulating.
        """
        target = strike.point() + strike.normal + self.randomInSphere()
        scattered = Ray(strike.point(), target)
        return Bounce(self.attenuation, scattered)
