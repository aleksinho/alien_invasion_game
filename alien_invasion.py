import sys
import pygame



class AlienInvasion:
    """ Overal class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 670))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(200)
            print(self.clock.get_fps())

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()