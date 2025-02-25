from abc import abstractmethod


# Base UI class
class UI:
    def __init__(self, x, y, width, height, scene_manager):
        self.scene_manager = scene_manager
        self.visible = True
        self.active = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def draw(self, screen):
        """ Implement it in child classes """
