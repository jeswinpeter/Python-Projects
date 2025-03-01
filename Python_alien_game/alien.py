import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribure.
        self.img = pg.image.load('D:/Python Projeccts/Python_alien_game/Images/Alien.bmp')
        org_size = self.img.get_size()
        scaled_size = (org_size[0] // 6, org_size[1] // 5)
        self.image = pg.transform.scale(self.img, scaled_size)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        