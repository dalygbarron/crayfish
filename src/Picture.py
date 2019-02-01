from Vector3 import *

class Picture:
    """Represents a 2D picture and can output it as well"""
    def __init__(self, x, y):
        self.content = []
        for iy in range(y):
            line = []
            for ix in range(x):
                line.append(Vector3())
            self.content.append(line)

    def pixel(self, x, y, colour = None):
        """Sets a pixel in the picture"""
        if (colour): self.content[y][x] = colour
        return self.content[y][x]

    def ppm(self):
        """Outputs the picture in ppm format to stdout"""
        print "P3"
        print len(self.content[0]), len(self.content)
        print 255
        for line in self.content:
            for item in line:
                print int(item.x * 255), int(item.y * 255), int(item.z * 255)
