import pygame as pg

from pygame import mixer

class Sounds():
    """ Class to handle sound effects """

    def __init__(self, ai_game):
        """ Start playing background music """
        self.stats = ai_game.stats
        self.play_bgm()

        # Loading bullet sound.
        self.bullet_sound = mixer.Sound("D:/Python Projeccts/Python_alien_game/Sounds/shot_ok.wav")
        
        # Loading explosioin sound
        self.ship_explode = mixer.Sound("D:/Python Projeccts/Python_alien_game/Sounds/explosion_ok_2.wav")

    def play_bgm(self):
        """ Play bgm according to state of the game. """
        if self.stats.game_active:
            mixer.music.load("D:/Python Projeccts/Python_alien_game/Sounds/active_bg.mp3")
            mixer.music.play(-1)
        else:
            mixer.music.load("D:/Python Projeccts/Python_alien_game/Sounds/inactive_bg.wav")
            mixer.music.play(-1)
    
    def fire_sound(self):
        """ Bullet sound effect """
        self.bullet_sound.play()

    def ship_explode_sound(self):
        """ Ship explosion sound effect. """
        self.ship_explode.play()