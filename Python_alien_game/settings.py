class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings 
        self.screen_width = 1600
        self.screen_height = 950
        self.bg_color = (7, 7, 7)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.ammo_limit = 10

        # Alien Settings
        self.fleet_drop_speed = 15
        

        # How quickly the game speeds up 
        self.speedup_scale = 1.4

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.5

        # Fleet direction od 1 represents right, and -1 means left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        """ Increase speed when leveling up. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale