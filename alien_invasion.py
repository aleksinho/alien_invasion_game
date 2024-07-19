import sys
import pygame



class AlienInvasion:
    """ Overal class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")