import pygame, sys
from pygame.locals import *

main_clock = pygame.time.Clock()

mixer.init()
while main_menu() is True:
    mixer.music.load('Music/mainmenu.wav')
    mixer.music.play()
# Play main menu music while main menu is loaded
while main_game() is True:
    mixer.music.load('Music/pianoplaylist.wav')
    mixer.music.play()
# Play piano playlist while game is loaded