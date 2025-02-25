import pygame

from ui.ui import *


class Text(UI):
    def __init__(self,x, y, width, height, scene_manager, text, font_size=35):
        super().__init__(x, y, width, height, scene_manager)
        self.font = pygame.font.SysFont(None, font_size)
        self.text = text
        self.color = scene_manager.themes['text-color']
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        if self.visible:
            screen.blit(self.surface, self.rect) # Render surface and rectangle if visible == True

    # Updating text by assigning new value for surface and new value for rectangle
    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

