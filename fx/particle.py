# imports --------------------------------------------------------------------------- #
import math
import random

import pygame

from ..object import Circle
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

        if len(colour) != 3:
            raise Exception

        # functionality ------------------------------------------------------------- #
        if type(colour) != tuple:
            colour = tuple(colour)

        self.__colour = colour

    @property
    def fade(self):
        # functionality ------------------------------------------------------------- #
        return self.__fade

    @fade.setter
    def fade(self, fade):
        # sanity checks ------------------------------------------------------------- #
        if type(fade) != bool:
            raise TypeError

        # functionality ------------------------------------------------------------- #
        self.__fade = fade

    @property
    def life(self):
        # functionality ------------------------------------------------------------- #
        return self.__life

    @life.setter
    def life(self, life):
        # sanity checks ------------------------------------------------------------- #
        if type(life) not in (float, int):
            raise TypeError

        if life < 0:
            raise Exception

        # functionality ------------------------------------------------------------- #
        self.__life = life

    @property
    def lower(self):
        # functionality ------------------------------------------------------------- #
        return self.__lower

    @lower.setter
    def lower(self, lower):
        # sanity checks ------------------------------------------------------------- #
        if type(lower) not in (float, int):
            raise TypeError

        try:
            if lower > self.__upper:
                raise Exception
        except AttributeError:
            pass

        # functionality ------------------------------------------------------------- #
        if type(lower) != int:
            lower = int(lower)

        self.__lower = lower

    @property
    def radius(self):
        # functionality ------------------------------------------------------------- #
        return self.__radius

    @radius.setter
    def radius(self, radius):
        # sanity checks ------------------------------------------------------------- #
        if type(radius) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(radius) != float:
            radius = float(radius)

        self.__radius = radius

    @property
    def rate(self):
        # functionality ------------------------------------------------------------- #
        return self.__rate

    @rate.setter
    def rate(self, rate):
        # sanity checks ------------------------------------------------------------- #
        if type(rate) not in (float, int):
            raise TypeError

        if rate < 0:
            raise Exception

        # functionality ------------------------------------------------------------- #
        if type(rate) != float:
            rate = float(rate)

        self.__rate = rate

    @property
    def speed(self):
        # functionality ------------------------------------------------------------- #
        return self.__speed

    @speed.setter
    def speed(self, speed):
        # sanity checks ------------------------------------------------------------- #
        if type(speed) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(speed) != float:
            speed = float(speed)

        self.__speed = speed

    @property
    def upper(self):
        # functionality ------------------------------------------------------------- #
        return self.__upper

    @upper.setter
    def upper(self, upper):
        # sanity checks ------------------------------------------------------------- #
        if type(upper) not in (float, int):
            raise TypeError

        try:
            if upper < self.__lower:
                raise Exception
        except AttributeError:
            pass

        # functionality ------------------------------------------------------------- #
        if type(upper) != int:
            upper = int(upper)

        self.__upper = upper

    # methods ----------------------------------------------------------------------- #
    def draw(self, surface, delta, offset=Vector(0, 0)):
        # sanity checks ------------------------------------------------------------- #
        if type(surface) != type(pygame.Surface([0, 0])):
            raise TypeError

        if type(delta) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
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
        # functionality ------------------------------------------------------------- #
        decay = (1 / delta) / self.life

        if self.fade:
            self.alpha = 255 * self.health

        self.health -= decay
        self.radius = self.start_radius * self.health

        self.centre += self.motion
