import pygame
from logic.functions import *

from entity.player import Player
from scenes.game_over_scene import GameOverScene
from scenes.game_scene import GameScene
from scenes.highscores_scene import HighscoresScene
from scenes.intro_scene import IntroScene
from scenes.menu_scene import MenuScene
from scenes.options_scene import OptionsScene
from scenes.credits_scene import CreditsScene
from scenes.pause_scene import PauseScene
from scenes.splash_scene import SplashScene

pygame.mixer.init()
pygame.display.init()
pygame.display.set_mode((960, 600))

# region COLORS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
# endregion
# region IMAGES
unmute = pygame.image.load('files/images/unmute_60.png').convert_alpha()
mute = pygame.image.load('files/images/mute_60.png').convert_alpha()
unmute_hover = pygame.image.load('files/images/unmute_hover_60.png').convert_alpha()
mute_hover = pygame.image.load('files/images/mute_hover_60.png').convert_alpha()
button_80 = pygame.image.load('files/images/button_80.png').convert_alpha()
button_160 = pygame.image.load('files/images/button_160.png').convert_alpha()
button_400 = pygame.image.load('files/images/button_400.png').convert_alpha()
hover_80 = pygame.image.load('files/images/hover_80.png').convert_alpha()
hover_160 = pygame.image.load('files/images/hover_160.png').convert_alpha()
hover_400 = pygame.image.load('files/images/hover_400.png').convert_alpha()
wrong_400 = pygame.image.load('files/images/wrong_400.png').convert_alpha()
correct_400 = pygame.image.load('files/images/correct_400.png').convert_alpha()
selected_80 = pygame.image.load('files/images/selected_80.png').convert_alpha()
bg_light = pygame.image.load('files/images/bg_light_strip.png').convert_alpha()
bg_medium = pygame.image.load('files/images/bg_medium_strip.png').convert_alpha()
bg_dark = pygame.image.load('files/images/bg_dark_strip.png').convert_alpha()
title_dark = pygame.image.load('files/images/title_dark.png').convert_alpha()
title_light = pygame.image.load('files/images/title_light.png').convert_alpha()

# endregion
# region SOUNDS
loop = pygame.mixer.Sound('files/sounds/loop.mp3')
click = pygame.mixer.Sound('files/sounds/click.mp3')
error = pygame.mixer.Sound('files/sounds/error.mp3')
correct = pygame.mixer.Sound('files/sounds/correct.mp3')
clock = pygame.mixer.Sound('files/sounds/clock.mp3')
times_up = pygame.mixer.Sound('files/sounds/times_up.mp3')

# endregion

class SceneManager:
    def __init__(self, screen):
        self.player = Player("Player")
        self.colors = {'red': RED, 'white': WHITE, 'black': BLACK, 'light-gray': LIGHT_GRAY, 'gray': GRAY, 'dark-gray': DARK_GRAY}
        self.themes = {'bg-color': LIGHT_GRAY, 'text-color': BLACK, 'title-image': title_dark}
        self.buttons = {'60': mute, '61': unmute, '80': button_80, '160': button_160, '400': button_400}
        self.hovers = {'60': mute_hover, '61': unmute_hover, '80': hover_80, '160': hover_160, '400': hover_400}
        self.utilities = {'w400': wrong_400, 'c400': correct_400, 's80': selected_80}
        self.backgrounds = {'Light': bg_light, 'Medium': bg_medium, 'Dark': bg_dark, 'title-dark': title_dark, 'title-light': title_light}
        self.sounds = {'click': click, 'error': error, 'correct': correct, 'clock': clock, 'times-up': times_up}
        self.theme_value = 'Light'
        self.mode_value = 'One game'
        self.current_scene = None
        self.is_correct = True
        self.last_update_time = pygame.time.get_ticks()
        self.max_questions = 10
        self.correct_to_level_up = 4
        self.correct_count = 0
        self.question_count = 1
        self.time_left = 30
        self.volume = 1.0
        self.screen = screen
        self.intro_scene = None
        self.menu_scene = None
        self.options_scene = None
        self.game_scene = None
        self.credits_scene = None
        self.highscores_scene = None
        self.pause_scene = None
        self.game_over_scene = None
        self.splash_scene = None
        self.events = None
        self.filename = 'files/easy.txt'
        loop.play(loops=-1)

    def set_events(self, events):
        self.events = events

    def start(self):
        self.intro_scene = IntroScene(self)
        self.menu_scene = MenuScene(self)
        self.options_scene = OptionsScene(self)
        self.game_scene = GameScene(self)
        self.credits_scene = CreditsScene(self)
        self.highscores_scene = HighscoresScene(self)
        self.pause_scene = PauseScene(self)
        self.game_over_scene = GameOverScene(self)
        self.splash_scene = SplashScene(self)
        self.current_scene = self.splash_scene
        self.current_scene.__init__(self)
        if self.current_scene == self.splash_scene:
            print(self.current_scene)
            self.current_scene.start()

    def update(self):
        if self.current_scene:
            times_up.set_volume(self.volume / 5)
            clock.set_volume(self.volume / 5)
            click.set_volume(self.volume)
            loop.set_volume(self.volume)
            error.set_volume(self.volume)
            correct.set_volume(self.volume)
            self.current_scene.update_scene()
            self.assign_theme_value()

    def switch_scene(self, new_scene):
        self.current_scene = new_scene
        new_scene.__init__(self)
        new_scene.start()

    def get_current_scene(self):
        return self.current_scene

    def get_theme(self):
        return self.themes

    def restart_game(self, scene):
        self.time_left = 30
        self.player.score += self.correct_count
        self.correct_count = 0
        self.question_count = 1
        self.switch_scene(scene)

    def check_level_up(self):
        return self.correct_count >= self.correct_to_level_up

    def countdown_timer(self):
        global clock
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= 1000 and self.time_left > 0:
            clock.stop()
            clock.play()
            self.time_left -= 1
            self.current_scene.background.animate(self.backgrounds[self.theme_value], 800, 600,
                                                  (self.screen.get_width(), self.screen.get_height()), 6)
            self.last_update_time = current_time
            self.current_scene.timer_text.update_text(str(self.time_left))
        if self.time_left == 0:
            self.time_left = -1
            times_up.play()
        if self.time_left <= 6:
            self.current_scene.timer_text.color = self.colors['red']

    def set_theme(self, bg_color, text_color, title_image):
        self.themes['bg-color'] = bg_color
        self.themes['text-color'] = text_color
        self.themes['title-image'] = title_image

    def assign_theme_value(self):
        match self.theme_value:
            case "Light":
                self.set_theme(self.colors['light-gray'], self.colors['black'], self.backgrounds['title-dark'])
            case "Medium":
                self.set_theme(self.colors['gray'], self.colors['white'], self.backgrounds['title-dark'])
            case "Dark":
                self.set_theme(self.colors['dark-gray'], self.colors['white'], self.backgrounds['title-light'])
