from pygame.examples.moveit import WIDTH

from scenes.base_scene import *


class MenuScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.start_button = Button(w // 2 - 80, h - 400, 160, 40, "Start", sm)
        self.options_button = Button(w // 2 - 80, h - 340, 160, 40, "Options", sm)
        self.credits_button = Button(w // 2 - 80, h - 280, 160, 40, "Credits", sm)
        self.highscores_button = Button(w // 2 - 80, h - 220, 160, 40, "Highscores", sm)
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)
        self.ui_list.extend([self.start_button, self.options_button, self.credits_button, self.highscores_button,
                             self.exit_button])
        self.button_scene_map = { # Mapping to dict Keys buttons and Values scenes to control action of button clicked
            self.exit_button: sm.intro_scene,
            self.options_button: sm.options_scene,
            self.start_button: sm.game_scene,
            self.credits_button: sm.credits_scene,
            self.highscores_button: sm.highscores_scene,
        }

    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event)

    def exit_scene(self, event):
        for button, scene in self.button_scene_map.items(): # for all keys values in map items
            if button.is_clicked(event, self.scene_manager.sounds['click']): # Corresponding button is clicked
                self.scene_manager.switch_scene(scene) # Switch to scene related to that button


