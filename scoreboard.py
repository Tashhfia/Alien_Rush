import pygame.font
from pygame.sprite import Group

from spaceShip import SpaceShip


class Scoreboard:
    def __init__(self, ai_game):
        """Initialize score-keeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.prep_spaceShips_left()

        self.text_color = (61, 235, 52)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = str(rounded_score)
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.spaceShips.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
        self.prep_high_score()

    def prep_spaceShips_left(self):
        self.spaceShips = Group()
        for spaceShip_num in range(self.stats.spaceShips_left):
            spaceShip = SpaceShip(self.ai_game)
            spaceShip.rect.x = 10 + spaceShip_num * spaceShip.rect.width
            spaceShip.rect.y = 10
            self.spaceShips.add(spaceShip)




