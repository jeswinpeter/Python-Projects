class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings 
        self.screen_width = 1600
        self.screen_height = 950
        self.bg_color = (7, 7, 7)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.ammo_limit = 12

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction od 1 represents right, and -1 means lefr
        self.fleet_direction = 1