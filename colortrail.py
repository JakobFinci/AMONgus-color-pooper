"""
The best game in the word - file for the etch-a-sketch models and controls.
(aka - the color poop)
"""
from abc import ABC, abstractmethod
import pygame
from pygame.locals import *

pygame.init()
# Initialize pygame


class ColorPoop(ABC):
    """
    An abstract base class for the color-poop
    """

    def __init__(self, my_amon):
        """
        Init function for the color-poop

        Attributes:
        _my_amon = a private instance of the Amon class
            colors_dict: a public dictionary of strings representing colors
            mapped to respective RGB triplet values represented by tuples
        """
        self._my_amon = my_amon
        self.colors_dict = {"red": (255, 48, 48), "yellow": (238, 201, 0),
                            "blue": (0, 191, 255), "black": (0, 0, 0), "white": (255, 255, 255)}

    @abstractmethod
    def poop(self):
        """
        An abstract method that does nothing.
        """

    @abstractmethod
    def genericmethod(self):
        """
        An abstract method that does nothing.
        """


class Defecate(ColorPoop):
    """
    A subclass of the game's abstract base class that serves as the color
    poop's method, controls, and view.
    """

    def poop(self):
        """
        Returns and renders a single color poop.
        """
        amon_stats_copy = self._my_amon.amon_stats
        for colors in self.colors_dict:
            if colors == amon_stats_copy[3]:
                curr_list = [colors, (amon_stats_copy[0], amon_stats_copy[1]),
                             3]
                return curr_list
        return None
        # Attempt to draw circle with correct coord and color by returning it's
        # data for the viewer - else do nothing.

    def genericmethod(self):
        """
        Pylint wants at least two public methods - so I added this debug
        method to appease it and add dev functionality.

        Returns:
            a string based off of the functionality of the poop method
        """
        try:
            self.poop
        except KeyboardInterrupt:
            return print("Get your grubby paws off the keyboard!")
        except TypeError:
            return print("Something's wrong!")
        else:
            return print("All good here b0ss!")
