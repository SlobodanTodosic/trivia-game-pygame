from typing import override

from scenes.base_scene import *
class PauseScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)
        self.ui_list.extend([self.exit_button])


    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event)

    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)

