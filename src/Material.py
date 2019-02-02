from Bounce import *

class Material:
    """Represents a material that modifies the colour a ray sees."""

    def scatter(self, ray):
        """
        Does the stuff that happens when a ray hits the material.
        It is meant to return a Bounce and if the bounce has no scatter ray then
        that means there are no more rays.
        """
        return Bounce()
