import sys

import pygame

from settings import Settings

def run_game():
    #Initialize game and create screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height)) #set the game screen size
    pygame.display.set_caption("Alien Invasion")

    while True:
        #listening keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    #Redraw the screen for each pass
    screen.fill(game_settings.bg_color)
    pygame.display.flip() #Make the most recently drawn screen visible

run_game()
