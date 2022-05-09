"""
The best game in the word - file for Amon's model and controls.
"""
import sys
import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()


class Amon:
    """
    A class containing Amon's model and controls
    """

    def __init__(self):
        """
        Init function for Amon

        Attributes:
            colors: a public list of possible colors Amon can become
            _xmovement: a private int describing Amon's movement on the x axis
            _ymovement: a private int describing Amon's movement on the y axis
            _color_counter: a private int representing the number of times Amon has switched
            colors
            _amon_stats: a private list containing statistics about Amon:
                - int representing x coord
                - int representing y coord
                - string representing current orientation
                - string from _colors list representing current color
            _amon_keystrokes: a private list for recording 11 most recent
            keystrokes
            _secret_counter: a private counter for counting secrets
        """
        self.colors = ["red", "yellow", "blue", "black", "white"]
        self._xmovement = 0
        self._ymovement = 0
        self._color_counter = 0
        self._amon_stats = [200, 200, "down",
                            self.colors[(self._color_counter % 5)]]
        self._amon_keystrokes = []
        self._secret_counter = 1

    @property
    def amon_stats(self):
        """
        A property method that returns a copy of _amon_stats
        """
        return self._amon_stats

    def edit_amon_stats(self,x,y,direction,color):
        '''
        A method for testing features dependent on amon_stats.
        
        Args: 
            x: x coordinate input
            y: y coordinate input
            direction: text direction input
            color: text color input
        '''
        self._amon_stats=[x, y, direction,color]

    def movement(self, event):
        """
        A method for moving Amon and changing his color.

        Args:
            event: an event that either can or cannot move
            Amon.
        """
        if event.key == pygame.K_LEFT:
            self._xmovement = -2
            self._amon_stats[2] = "left"
        if event.key == pygame.K_RIGHT:
            self._xmovement = 2
            self._amon_stats[2] = "right"
        if event.key == pygame.K_UP:
            self._ymovement = -2
            self._amon_stats[2] = "up"
        if event.key == pygame.K_DOWN:
            self._ymovement = 2
            self._amon_stats[2] = "down"
        # Detect movement and respond appropriately
        if event.key == pygame.K_SPACE:
            self._color_counter += 1
            self._amon_stats[3] = self.colors[(self._color_counter % 5)]
        # Detect space and change color accordingly

    def easter_egg(self):
        """
        Activates an easter egg. 'Nuff said.
        """
        self._amon_stats[2] = "secret"
        self._amon_keystrokes = []
        pygame.mixer.Channel(1).play(
            pygame.mixer.Sound(f"Music/{self._secret_counter}.wav"))
        self._secret_counter += 1
        if self._secret_counter == 9:
            self._secret_counter = 1

    def update_x_and_y(self, x_amount, y_amount):
        """
        A method for adjusting the private variables
        _xmovement and _ymovement for pytests.

        Args:
            x_amount: amount to adjust the _xmovement by.
            y_amount: amount to adjust the _ymovement by.
        """
        self._xmovement += x_amount
        self._ymovement += y_amount

    def amon_passive_update(self):
        """
        A method containing actions Amon does to update position and
        movement correctly per tick. These are:
        a) reset x and y position if out of bounds
        b) update position based on current movement attributes
        c) reset movement attributes if no input is detected
        """
        if self._amon_stats[0] < 20:
            self._amon_stats[0] = 20
        if self._amon_stats[1] < 24:
            self._amon_stats[1] = 24
        if self._amon_stats[0] > 478:
            self._amon_stats[0] = 478
        if self._amon_stats[1] > 472:
            self._amon_stats[1] = 472
        # Reset x and y position to inbounds if out of bounds
        if self._xmovement != 0:
            self._amon_stats[0] += self._xmovement
        if self._ymovement != 0:
            self._amon_stats[1] += self._ymovement
        # Update position based on current movement attributes
        if pygame.key.get_pressed()[K_LEFT] is False and \
            pygame.key.get_pressed()[K_RIGHT] is False and \
                pygame.key.get_pressed()[K_UP] is False and \
                    pygame.key.get_pressed()[K_DOWN] is False:
            self._xmovement = 0
            self._ymovement = 0
        # Reset x and y movement attributes if keyboard is not being pressed.

    def amon_mc(self):
        """
        A method containing Amon's model and controls
        """
        self.amon_passive_update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._amon_keystrokes.append(event.key)
                if len(self._amon_keystrokes) > 11:
                    for _ in range(len(self._amon_keystrokes) - 11):
                        del self._amon_keystrokes[0]
                # Record Amon's keystrokes
                if self._amon_keystrokes == [K_UP, K_UP, K_DOWN, K_DOWN,
                                             K_LEFT, K_RIGHT, K_LEFT, K_RIGHT, K_b, K_a, K_SPACE]:
                    self.easter_egg()
                    continue
                    # Play easter egg if secret code is detected
                self.movement(event)
                # Update color, movement, and position.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Give Amon the key to escape existance and therefore suffering


class AmonView(pygame.sprite.Sprite):
    """
    A class to help the viewer render Amon. Connects overall viewer in
    game.py to Amon's models and controls in class Amon.
    """

    def __init__(self, linking_amon):
        """
        Init function for Amon's Viewer

        Args:
            linking_amon: an instance of the Amon class so we can connect the
            MC in it with the V in this class.

        Attributes:
            Based off of the norm with pygame sprites - we initialize a pygame
            surface and a pygame rectangle as well as defining a class instance
            of Amon to link the MC with the V.
            Variables are all public due to the nature of standard practice of
            PyGame sprites.
        """
        self.linking_amon = linking_amon
        super().__init__()
        self.image = pygame.image.load(
            f"Images/{linking_amon.amon_stats[3]}/{linking_amon.amon_stats[2]}.png")
        # Set up sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [linking_amon.amon_stats[0],
                            linking_amon.amon_stats[1]]
        # Set up sprite rectangle

    def update(self, linking_amon):
        """
        A pygame update method to update the location and appearance of Amon based off of the input
        from the linking_amon's MC.
        """
        self.image = pygame.image.load(
            f"Images/{linking_amon.amon_stats[3]}/{linking_amon.amon_stats[2]}.png")
        if 20 < linking_amon.amon_stats[0] < 478 and 24 < linking_amon.amon_stats[1] < 472:
            self.rect.center = [linking_amon.amon_stats[0],
                                linking_amon.amon_stats[1]]
        if linking_amon.amon_stats[0] < 20:
            self.rect.center = [20,linking_amon.amon_stats[1]]
        if linking_amon.amon_stats[0] > 478:
            self.rect.center = [478,linking_amon.amon_stats[1]]
        if linking_amon.amon_stats[1] < 24 :
            self.rect.center = [linking_amon.amon_stats[0],24]
        if linking_amon.amon_stats[1] > 472:
            self.rect.center = [linking_amon.amon_stats[0],472]
        # We check to see if Amon stats is out of bounds. If so, we update the sprite rect
        # to be in bounds. Else, we update normally.

    def poot(self):
        """
        A method to allow Amon to have healthy bowel movements.
        Also pygame gets angry if I have less than two public methods.

        Returns:
            a list of data about Amon's bowel movement for the circle viewer.
        """
        return [(102, 90, 44), (self.linking_amon.amon_stats[0], \
            self.linking_amon.amon_stats[1]), 75]
