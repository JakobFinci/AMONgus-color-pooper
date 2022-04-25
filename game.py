import pygame, sys
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()
# Initialize pygame and music mixer

main_clock = pygame.time.Clock()
# Create game clock

main_font = pygame.font.SysFont("comic.ttf", 20)
screen = pygame.display.set_mode((500, 500),0,32)
# Create variables for ease of drawing text

def draw_text(text, color, x, y, font=main_font, surface=screen):
    """
    A function for drawing text with pygame.

    Args:
        text: a string containing the text to be drawn.
        color: a tuple with three int values representing
        RGB color.
        x: integer representing the x position of the text.
        y: integer representing the x position of the text.
        font: the font to use (use variable "font").
        surface: the surface to draw on (use variable "screen").
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    """

    """
    while True:
 
        screen.fill((0,0,0))
        draw_text('AMON(gus) Color Pooper', (255, 255, 255), 20, 20)
        draw_text('An artistic experience', (255, 255, 255), 20, 20)
        # Fill screen and make text

        mx, my = pygame.mouse.get_pos()
 
        button = pygame.Rect(50, 100, 200, 50)
        if button.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.rect(screen, (255, 0, 0), button)
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
 
        pygame.display.update()
        main_clock.tick(60)
        # Create game clock
        mixer.music.load("Music/mainmenu.wav")
        mixer.music.play()
        # Play main menu music while main menu is loaded

main_menu()

while main_game() is True:
    mixer.music.load("Music/pianoplaylist.wav")
    mixer.music.play()
# Play piano playlist while game is loaded