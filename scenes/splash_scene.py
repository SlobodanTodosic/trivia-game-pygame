import pygame.time

from scenes.base_scene import *

scale = .5
direction = 2

class SplashScene(BaseScene):
    def __init__(self, sm, logo_w=30, logo_h=15):
        super().__init__(sm)
        self.w = logo_w
        self.h = logo_h
        self.title.y = 0
        # Creating UI elements
        self.title.image = pygame.transform.smoothscale(sm.themes['title-image'],(self.w, self.h))
        self.title.rect = self.title.image.get_rect(center=(self.title.x, self.title.y))
        self.time_left = 5

    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        self.logo_path()
        self.exit_scene(None)

    def exit_scene(self, event):
        current_time = pygame.time.get_ticks()
        # Splash screen timer
        if current_time - self.scene_manager.last_update_time >= 1000 and self.time_left > 0:
            self.time_left -= 1
            self.scene_manager.last_update_time = current_time
        elif self.time_left == 0:
            self.scene_manager.switch_scene(self.scene_manager.intro_scene)

    # Functon to animate logo path for splash screen
    def logo_path(self):
        global scale, direction

        max_w = 550
        max_h = 275
        min_x = 480
        max_x = 860
        max_y = 300

        self.w = min(self.w + scale / 4, max_w)
        self.h = min(self.h + scale / 8, max_h)
        self.title.y = min(self.title.y + .11, max_y)
        self.title.x = max(min(self.title.x + direction / 6.9, max_x), min_x)
        if self.title.x == max_x:
            direction = -2
        scale += .0002
        self.title.image = pygame.transform.smoothscale(self.scene_manager.themes['title-image'],
                                                        (self.w, self.h))
        self.title.rect = self.title.image.get_rect(center=(self.title.x, self.title.y))


