from scenes.base_scene import *
from ui.textfield import TextField


class IntroScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.button = Button(w // 2 - 80, h - 80, 160, 40, "Save and continue", sm)
        self.enter_text = Text(w // 2 - 100, h - 400, 0, 0, sm, "Enter nickname",40)
        self.text_field = TextField(w // 2 + 20, h - 420, 240, 40, sm)
        self.ui_list.extend([self.button, self.enter_text, self.text_field])

    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            # Checking to change the name of a player
            button_clicked = self.button.is_clicked(event, self.scene_manager.sounds['click'])
            length_not_zero = self.text_field.text != "" # Return False if textfield is empty
            if button_clicked and length_not_zero:
                self.scene_manager.player.name = self.text_field.text # Return new name if not empty
            self.exit_scene(event)
            self.text_field.handle_event(event) # Calling function to handle typing, backspace and other textfield events

    def exit_scene(self, event):
        if self.button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)
