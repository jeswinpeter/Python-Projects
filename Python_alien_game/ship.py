import pygame as pg

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.img = pg.image.load('D:/Python Projeccts/Python_alien_game/Images/Space_ship.bmp')
        org_size = self.img.get_size()
        scaled_size = (org_size[0] // 3, org_size[1] // 3) # Scaling the image
        self.image = pg.transform.scale(self.img, scaled_size)
        self.rect = self.image.get_rect()

 
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)