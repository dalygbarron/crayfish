from Vector3 import *
from Ray import *
from Sphere import *
from Strike import *
from Roster import *
from Eye import *
from Lambert import *
from Metal import *
from Texture import *
from Colour import *
from Checker import *
from Picture import *
import math
import random

min = 0.001
max = 10000000
bounceDepth = 50


def colour(ray, roster, depth = 0):
    strike = roster.hit(ray, min, max)
    if (strike):
        bounce = strike.medium.material.scatter(strike)
        if (depth >= bounceDepth): return Vector3()
        if (not bounce.scatter): return bounce.attenuation
        return colour(bounce.scatter, roster, depth + 1) * bounce.attenuation
    else:
        unitDirection = ray.direction.unit()
        t = (unitDirection.y + 1.0) / 2
        return  Vector3(1.0, 1.0, 1.0) * (1.0 - t) + Vector3(0.1, 0.2, 0.8) * t



frames = 1
width = 600
height = 600
samples = 2
pic = Picture(width, height * frames)

check = Checker(Vector3(0.0, 0.0, 0.3), Vector3(0.9, 0.9, 0.8))
gold = Colour(Vector3(0.8, 0.6, 0.4))
blue = Colour(Vector3(0.8, 0.3, 0.3))

roster = Roster()
brick = Lambert(blue)
grass = Lambert(check)
mirror = Metal(gold)

roster.add(Sphere(brick, Vector3(0.0, 0.0, 0.0), 0.5))
roster.add(Sphere(grass, Vector3(0.0, -100.5, 0.0), 100.0))
roster.add(Sphere(mirror, Vector3(1.0, 0.0, 0.0), 0.5))
roster.add(Sphere(mirror, Vector3(-1.0, 0.0, 0.0), 0.5))

for f in range(frames):
    eye = Eye(Vector3(2.0, 0.0 + float(f) * 0.5, 10.0), Vector3(0.0, 0.0, -1.0), Vector3(0.0, 1.0, 0.0), math.pi / 2, float(width) / float(height))
    for x in range(width):
        for y in range(height):
            col = Vector3()
            for s in range(samples):
                u = (x + random.random()) / float(width)
                v = (y + random.random()) / float(height)
                ray = eye.getRay(u, v)
                col += colour(ray, roster)
            col /= samples
            pic.pixel(x, y + height * f, col)

pic.ppm()
