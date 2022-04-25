import pygame, sys
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()
# Initialize pygame and music mixer

class GameArch:
    """
    A class containing the game's architecture.
    """

    click = False

    def __init__(self):
        """
        """
        self._main_clock = pygame.time.Clock()
        self._main_font = pygame.font.SysFont("Fonts/comic.ttf", 20)
        self._screen = pygame.display.set_mode((500, 500),0,32)

    def draw_text(self, text, color, x, y):
        """
        A method for drawing text with pygame.

        Args:
            text: a string containing the text to be drawn.
            color: a tuple with three int values representing
            RGB color.
            x: integer representing the x position of the text.
            y: integer representing the x position of the text.
            font: the font to use (use variable "font").
            surface: the surface to draw on (use variable "screen").
        """
        textobj = self._main_font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._screen.blit(textobj, textrect)

    def main_menu(self):
        """
        A method representing the main menu of the game.
        """
        while True:
            
            self._screen.fill((0,0,0))
            self.draw_text('AMON(gus) Color Pooper', (255, 255, 255), 20, 20)
            self.draw_text('An artistic experience', (255, 255, 255), 20, 20)
            # Fill screen and make text

            mx, my = pygame.mouse.get_pos()
    
            button = pygame.Rect(50, 100, 200, 50)
            if button.collidepoint((mx, my)):
                if click:
                    game()
            pygame.draw.rect(self._screen, (255, 0, 0), button)
            # Create button to start game

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            # Provide method for user to exit out of game

            mixer.music.load("Music/mainmenu.wav")
            mixer.music.play()
            # Play main menu music while main menu is loaded
            pygame.display.update()
            self._main_clock.tick(60)
            # Create game clock

if __name__ == "__main__":
    GameArch().main_menu()
# Initialize the game by starting the main menu

    while main_game() is True:
        mixer.music.load("Music/pianoplaylist.wav")
        mixer.music.play()
    # Play piano playlist while game is loaded