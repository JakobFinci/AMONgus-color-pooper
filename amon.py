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
            _music_channel: private music channel for playing music
            in
        """
        self.colors = ["red", "yellow", "blue", "black", "white"]
        self._color_counter = 0
        self._amon_stats = [200, 200, "down",
                            self.colors[(self._color_counter % 5)]]
        self._amon_keystrokes = []
        self._secret_counter = 1
        self._amon_channel = pygame.mixer.Channel(1)

    @property
    def amon_stats(self):
        """
        A property method that returns a copy of _amon_stats
        """
        return self._amon_stats

    def movement(self, event):
        """
        A method for moving Amon and changing his color.

        Args:
            event: an event that either can or cannot move
            Amon.
        """
        if event.key == pygame.K_LEFT:
            self._amon_stats[0] -= 2
            self._amon_stats[2] = "left"
        if event.key == pygame.K_RIGHT:
            self._amon_stats[0] += 2
            self._amon_stats[2] = "right"
        if event.key == pygame.K_UP:
            self._amon_stats[1] -= 2
            self._amon_stats[2] = "up"
        if event.key == pygame.K_DOWN:
            self._amon_stats[1] += 2
            self._amon_stats[2] = "down"
        # Detect movement and respond appropriately
        if self._amon_stats[0] < 0:
            self._amon_stats[0] = 0
        if self._amon_stats[1] < 0:
            self._amon_stats[1] = 0
        if self._amon_stats[0] > 500:
            self._amon_stats[0] = 500
        if self._amon_stats[1] > 500:
            self._amon_stats[1] = 500
        # Reset x and y position to inbounds if out of bounds
        if event.key == pygame.K_SPACE:
            self._color_counter += 1
            self._amon_stats[3] = self.colors[(self._color_counter % 5)]
        # Detect space and change color accordingly

    def amon_mc(self):
        """
        A method containing Amon's model and controls
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._amon_keystrokes.append(event.key)
                if len(self._amon_keystrokes) > 11:
                    for _ in range(len(self._amon_keystrokes) - 11):
                        del self._amon_keystrokes[0]
                # Record Amon's keystrokes
                if self._amon_keystrokes == [K_UP, K_UP, K_DOWN, K_DOWN,
                                             K_LEFT, K_RIGHT, K_LEFT, K_RIGHT, K_b, K_a, K_SPACE]:
                    self._amon_keystrokes = []
                    self._amon_stats[2] = "secret"
                    self._amon_channel.play(
                        pygame.mixer.Sound(f"Music/{self._secret_counter}.wav"))
                    self._secret_counter += 1
                    if self._secret_counter == 9:
                        self._secret_counter = 1
                    pygame.time.delay(4000)
                    self._amon_stats[2] = "down"
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
            of Amon to link the MC with the V
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
        self.rect.center = [linking_amon.amon_stats[0],
                            linking_amon.amon_stats[1]]

    def poot(self):
        """
        A method to allow Amon to have healthy bowel movements.
        Also pygame gets angry if I have less than two public methods.

        Returns:
            a list of data about Amon's bowel movement for the circle viewer.
        """
        return [(102,90,44),(self._amon_stats[0],self._amon_stats[1]),50]
