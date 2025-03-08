from typing import override

from scenes.base_scene import *
class PauseScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.pause_text = Text(w // 2, h // 2 - 80, 0, 0, sm, "GAME PAUSED", 35)
        self.pause_text_1 = Text(w // 2, h // 2 - 40, 0, 0, sm, "Logic to be applied in next iteration.", 20)
        self.pause_text_2 = Text(w // 2, h // 2 - 10, 0, 0, sm, "For now only back to menu scene possible", 20)
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)
        self.ui_list.extend([self.exit_button, self.pause_text, self.pause_text_1, self.pause_text_2])


    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event)

    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)

