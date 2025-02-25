import pygame

from logic.functions import get_image
from ui.ui import UI
# Creating the
class Background(UI):
    def __init__(self, x, y, width, height, scene_manager, image):
        super().__init__(x, y, width, height, scene_manager)
        self.image = image
        self.current_frame = 0
        self.rect = self.image.get_rect(center=(x, y)) # Creating rectangle for button


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) # Attaching image to the screen

    def change(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Simple animation by changing the frames
    def animate(self, theme, width, height, size, no_of_frames):
        self.image = pygame.transform.smoothscale(get_image(theme, width, height, self.current_frame), size)
        self.current_frame += 1
        if self.current_frame == no_of_frames: # If there are no more frames resetting to the first one
            self.current_frame = 0