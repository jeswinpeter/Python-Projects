class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings 
        self.screen_width = 1600
        self.screen_height = 950
        self.bg_color = (75, 30, 230)

        # Ship settings
        self.ship_speed = 1.5