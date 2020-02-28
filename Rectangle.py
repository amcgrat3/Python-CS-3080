import Shape
from Shape import *

class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    def Draw(self):
        super().Draw()
        for i in range(0, self.height):
            print("*" * self.width)