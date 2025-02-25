import pygame
from ui.ui import *

class TextField(UI):
    def __init__(self, x, y, width, height,scene_manager):
        super().__init__(x, y, width, height, scene_manager)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, 30)
        self.text = ""
        self.text_color = (30, 30, 30)
        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.active = False

    def handle_event(self, event):
        pygame.key.set_repeat(400, 50) # Enable continuous typing if button held
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos): # If Textfield is clicked change to active
                self.active = True
            else:
                self.active = False # If clicked outside textfield sets inactive
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1] # Deleting text from the right end side
            elif len(self.text) < 10:
                self.text += event.unicode # Typing text

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)
        if self.active:
            pygame.draw.rect(screen, self.border_color, self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 10))