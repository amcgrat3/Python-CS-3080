import Shape
from Shape import *

class Triangle(Shape):

    def __init__(self, base):
        self._base = int(base)

    def Draw(self):
        super().Draw()
        for i in range(1, self._base + 1):
            print("*" * int(i))

