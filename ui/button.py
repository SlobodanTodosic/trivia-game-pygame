import pygame
from ui.ui import *

class Button(UI):
    def __init__(self, x, y, width, height, text, scene_manager, visible=True, active=True):
        super().__init__(x, y, width, height, scene_manager)
        self.image = scene_manager.buttons[str(width)]
        self.hover = scene_manager.hovers[str(width)]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.visible = visible
        self.active = active
        self.font = pygame.font.SysFont("Consolas", 16) # Font creation
        # Rendering the font on surface
        self.text_surface = self.font.render(self.text, True, scene_manager.colors['white'])
        self.text_rect = self.text_surface.get_rect(center=self.rect.center) # Creating rectangle for Text

    def draw(self, screen):
        if not self.visible:
            return
        mouse_position = pygame.mouse.get_pos() # Returning mouse position
        if self.rect.collidepoint(mouse_position): # If mouse position is inside the button frames
            screen.blit(self.hover, (self.rect.x, self.rect.y)) # Render hover image
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y)) # Render base image
        screen.blit(self.text_surface, self.text_rect) # Render text on the screen

    def is_clicked(self, event, sound):
        if not self.active: # If not active unable to click
            return
        # If button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            sound.play()
            return True
        return False

    def set_visual_no_hover(self, size):
        self.image = self.scene_manager.utilities[size]
        self.hover = self.scene_manager.utilities[size]

    def set_visual_hover(self, size):
        self.image = self.scene_manager.buttons[size]
        self.hover = self.scene_manager.hovers[size]

    def update_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.scene_manager.colors['white'])
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
