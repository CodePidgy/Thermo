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
        # functionality ------------------------------------------------------------- #
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        # sanity checks ------------------------------------------------------------- #
        if type(alpha) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(alpha) != int:
            alpha = int(alpha)

        self.__alpha = alpha

    @property
    def centre(self):
        # functionality ------------------------------------------------------------- #
        return self.__centre

    @centre.setter
    def centre(self, centre):
        # sanity checks ------------------------------------------------------------- #
        if type(centre) != type(Vector()):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        self.__centre = centre

    @property
    def colour(self):
        # functionality ------------------------------------------------------------- #
        return self.__colour

    @colour.setter
    def colour(self, colour):
        # sanity checks ------------------------------------------------------------- #
        if type(colour) not in (list, tuple):
            raise TypeError

        if len(colour) > 4 or len(colour) < 3:
            raise Exception

        # functionality ------------------------------------------------------------- #
        if type(colour) != tuple:
            colour = tuple(colour)

        self.__alpha = 255

        if len(colour) != 3:
            self.__alpha = colour[3]
            colour = colour[:3]

        self.__colour = colour

    @property
    def radius(self):
        # functionality ------------------------------------------------------------- #
        return self.__radius

    @radius.setter
    def radius(self, radius):
        # sanity checks ------------------------------------------------------------- #
        if type(radius) not in (float, int):
            raise Exception

        # functionality ------------------------------------------------------------- #
        if type(radius) != float:
            radius = float(radius)

        self.__radius = radius

    @property
    def rect(self):
        # functionality ------------------------------------------------------------- #
        return Rect(
            self.x - self.__radius,
            self.y - self.__radius,
            self.__radius * 2,
            self.__radius * 2,
        )

    @property
    def width(self):
        # functionality ------------------------------------------------------------- #
        return self.__width

    @width.setter
    def width(self, width):
        # sanity checks ------------------------------------------------------------- #
        if type(width) != int:
            raise TypeError

        # functionality ------------------------------------------------------------- #
        self.__width = width

    @property
    def x(self):
        # functionality ------------------------------------------------------------- #
        return self.__centre.x

    @x.setter
    def x(self, x):
        # sanity checks ------------------------------------------------------------- #
        if type(x) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(x) != float:
            x = float(x)

        self.__centre.x = x

    @property
    def y(self):
        # functionality ------------------------------------------------------------- #
        return self.__centre.y

    @y.setter
    def y(self, y):
        # sanity checks ------------------------------------------------------------- #
        if type(y) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(y) != float:
            y = float(y)

        self.__centre.y = y

    # methods ----------------------------------------------------------------------- #
    def draw(self, surface, offset=Vector(0, 0)):
        # sanity checks ------------------------------------------------------------- #
        if type(surface) != type(pygame.Surface([0, 0])):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__alpha == 255:
            pygame.draw.circle(
                surface, self.__colour, [*(self.centre + offset)], self.__radius, self.__width
            )
        else:
            temp_surface = self.rect.pygame_surface().convert_alpha()

            temp_surface.fill([0, 0, 0, 0])
            temp_surface.set_alpha(self.__alpha)

            pygame.draw.circle(
                temp_surface,
                self.__colour,
                [*self.rect.size / 2],
                self.__radius,
                self.__width,
            )

            surface.blit(
                temp_surface,
                [
                    self.x - self.rect.width / 2 + offset.x,
                    self.y - self.rect.height / 2 + offset.y,
                ],
            )
