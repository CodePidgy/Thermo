# imports --------------------------------------------------------------------------- #
import math
import random

import pygame

from ..shape import Circle
from ..vector import Vector


# particle class -------------------------------------------------------------------- #
class Particle:
    # initialisation ---------------------------------------------------------------- #
    def __init__(
        self,
        centre: Vector,
        radius: float,
        colour: tuple,
        rate: float,
        life: float,
        lower: int,
        upper: int,
        speed: float,
        fade: bool,
    ):
        self.centre = centre
        self.colour = colour
        self.fade = fade
        self.life = life
        self.lower = lower
        self.radius = radius
        self.rate = rate
        self.speed = speed
        self.upper = upper

        self.__children = []
        self.__timer = 0.0

    # properties -------------------------------------------------------------------- #
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

        if len(colour) != 3:
            raise Exception

        if type(colour) != tuple:
            colour = tuple(colour)

        self.__colour = colour

    @property
    def fade(self):
        return self.__fade

    @fade.setter
    def fade(self, fade):
        if type(fade) != bool:
            raise TypeError

        self.__fade = fade

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life):
        if type(life) not in (float, int):
            raise TypeError

        if life < 0:
            raise Exception

        self.__life = life

    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower):
        if type(lower) not in (float, int):
            raise TypeError

        try:
            if lower > self.__upper:
                raise Exception
        except AttributeError:
            pass

        if type(lower) != int:
            lower = int(lower)

        self.__lower = lower

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if type(radius) not in (float, int):
            raise TypeError

        if type(radius) != float:
            radius = float(radius)

        self.__radius = radius

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        if type(rate) not in (float, int):
            raise TypeError

        if rate < 0:
            raise Exception

        if type(rate) != float:
            rate = float(rate)

        self.__rate = rate

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if type(speed) not in (float, int):
            raise TypeError

        if type(speed) != float:
            speed = float(speed)

        self.__speed = speed

    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper):
        if type(upper) not in (float, int):
            raise TypeError

        try:
            if upper < self.__lower:
                raise Exception
        except AttributeError:
            pass

        if type(upper) != int:
            upper = int(upper)

        self.__upper = upper

    # methods ----------------------------------------------------------------------- #
    def draw(self, surface, delta, offset=Vector(0, 0)):
        if type(surface) != type(pygame.Surface([0, 0])):
            raise TypeError

        if type(delta) not in (float, int):
            raise TypeError

        for child in self.__children:
            child.draw(surface)

        self.__timer += 1
        spawn = delta / self.__rate

        while self.__timer >= spawn:
            self.__timer -= spawn

            angle = math.radians(random.randrange(self.__lower, self.__upper))

            self.__children.append(
                Child(
                    self.__centre + offset,
                    self.__radius,
                    self.__colour,
                    self.__life,
                    Vector(math.cos(angle), math.sin(angle)) * self.__speed,
                    self.__fade,
                )
            )

        for child in self.__children:
            child.update(delta)

            if child.health <= 0:
                self.__children.remove(child)


# child class ----------------------------------------------------------------------- #
class Child(Circle):
    # initialisation ---------------------------------------------------------------- #
    def __init__(self, centre, radius, colour, life, motion, fade):
        super().__init__(centre, radius, colour)
        self.fade = fade
        self.health = 1
        self.life = life
        self.motion = motion
        self.start_radius = radius

    # methods ----------------------------------------------------------------------- #
    def update(self, delta):
        decay = (1 / delta) / self.life

        if self.fade:
            self.alpha = 255 * self.health

        self.health -= decay
        self.radius = self.start_radius * self.health

        self.centre += self.motion
