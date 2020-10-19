# imports --------------------------------------------------------------------------- #
import pygame

from .rect import Rect
from ..vector import Vector

# circle class ---------------------------------------------------------------------- #
class Circle:
    # initialisation ---------------------------------------------------------------- #
    def __init__(
        self,
        centre: Vector,
        radius: float,
        colour: list,
        width: int = 0,
    ):
        self.centre = centre
        self.colour = colour
        self.radius = radius
        self.width = width

    # properties -------------------------------------------------------------------- #
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        if type(alpha) not in (float, int):
            raise TypeError

        if type(alpha) != int:
            alpha = int(alpha)

        self.__alpha = alpha

    @property
    def centre(self):
        return self.__centre

    @centre.setter
    def centre(self, centre):
        if type(centre) != type(Vector()):
            raise TypeError

        self.__centre = centre

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        if type(colour) not in (list, tuple):
            raise TypeError

        if len(colour) > 4 or len(colour) < 3:
            raise Exception

        if type(colour) != tuple:
            colour = tuple(colour)

        self.__alpha = 255

        if len(colour) != 3:
            self.__alpha = colour[3]
            colour = colour[:3]

        self.__colour = colour

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if type(radius) not in (float, int):
            raise Exception

        if type(radius) != float:
            radius = float(radius)

        self.__radius = radius

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError

        self.__width = width

    @property
    def x(self):
        return self.__centre.x

    @x.setter
    def x(self, x):
        if type(x) not in (float, int):
            raise TypeError

        if type(x) != float:
            x = float(x)

        self.__centre.x = x

    @property
    def y(self):
        return self.__centre.y

    @y.setter
    def y(self, y):
        if type(y) not in (float, int):
            raise TypeError

        if type(y) != float:
            y = float(y)

        self.__centre.y = y

    # methods ----------------------------------------------------------------------- #
    def draw(self, surface, offset=Vector(0, 0)):
        if type(surface) != type(pygame.Surface([0, 0])):
            raise TypeError

        pygame.draw.circle(
            surface,
            [*self.__colour, max(self.__alpha, 0)],
            [*(self.centre + offset)],
            self.__radius,
            self.__width,
        )

    def rect(self):
        return Rect(
            self.x - self.__radius,
            self.y - self.__radius,
            self.__radius * 2,
            self.__radius * 2,
        )
