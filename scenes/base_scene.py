from abc import ABC, abstractmethod
import pygame
from matplotlib.pyplot import title

from ui.image import Image
from ui.text import Text
from ui.button import Button
from logic.functions import *


class BaseScene(ABC):
    def __init__(self, sm):
        self.scene_manager = sm
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.mute_button = Button(w - 80, 20, 60, 40, "", sm, False, False)
        self.mute_button.set_visual_hover('60' if sm.volume == 1 else '61')
        self.title = Image(w // 2, 100, 200, 100, sm, sm.themes['title-image'])
        self.background = Image(w // 2, h // 2, w, h, sm,
                                pygame.transform.smoothscale(
                                         get_image(sm.backgrounds[sm.theme_value],
                                                   800, 600), (w, h)))
        self.ui_list = [self.background, self.title, self.mute_button]

    # Draw or render UI to the screen
    def draw(self):
        for ui in self.ui_list:
            ui.draw(self.scene_manager.screen)

    @abstractmethod
    def start(self):
        """Abstract method - must be implemented by child classes"""

    def update_scene(self): # Update method to handle events
        for event in self.scene_manager.events:
            # Change visual of mute/unmute button on click
            if self.mute_button.is_clicked(event, self.scene_manager.sounds['click']):
                if self.mute_button.image == self.scene_manager.buttons['60']:
                    self.scene_manager.volume = 0.0
                    self.mute_button.set_visual_hover('61')
                else:
                    self.scene_manager.volume = 1.0
                    self.mute_button.set_visual_hover('60')
        self.draw() # Draw all UI elements to be up to date

    # Function to define exit condition
    @abstractmethod
    def exit_scene(self, event):
        """Abstract method - must be implemented by child classes"""
