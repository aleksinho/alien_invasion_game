import sys
import pygame
from settings import Settings
from ship import Ship



class AlienInvasion:
    """ Overal class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Initial view of screen is not flscr(false), in case of True it is flscr
        self.fullscreen_mode = False

        # # Fullscreen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """ Start the main loop for the game` """
        while True:
            self._check_events()
            self.ship.update(self)
            self._update_screen()
            # fps
            self.clock.tick(60)
            print(self.clock.get_fps())

    def _check_events(self):
        """ Responds to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            self.fullscreen_mode = True if self.fullscreen_mode == False else False
            self._fullscreen_mode()

    def _check_keyup_events(self, event):
        """ Respond to keyreleases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fullscreen_mode(self):
        initial_screen = self.screen
        if self.fullscreen_mode:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()