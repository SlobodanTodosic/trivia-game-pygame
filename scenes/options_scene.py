from scenes.base_scene import *

class OptionsScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.number_text = Text(w // 2, h - 425, 0,0, sm, "Number of questions? (One game mode only)", 25)
        self.ten_button = Button(w // 2 - 160, h - 410, 80, 40, "10", sm)
        self.twenty_button = Button(w // 2 - 40, h - 410, 80, 40, "20", sm)
        self.thirty_button = Button(w // 2 + 80, h - 410, 80, 40, "30", sm)

        self.theme_text = Text(w // 2, h - 340, 0, 0, sm, "Chose theme", 25)
        self.light_button = Button(w // 2 - 160, h - 325, 80, 40, "Light", sm)
        self.medium_button = Button(w // 2 - 40, h - 325, 80, 40, "Medium", sm)
        self.dark_button = Button(w // 2 + 80, h - 325, 80, 40, "Dark", sm)

        self.mode_text = Text(w // 2, h - 255, 0, 0, sm, "Chose mode", 25)
        self.one_game = Button(w // 2 - 160, h - 240, 80, 40, "One game", sm)
        self.level_up = Button(w // 2 - 40, h - 240, 80, 40, "Level up", sm)
        self.no_error = Button(w // 2 + 80, h - 240, 80, 40, "No error", sm)

        self.difficulty = Text(w // 2, h - 170, 0, 0, sm, "Difficulty", 25)
        self.easy_btn = Button(w // 2 - 160, h - 155, 80, 40, "Easy", sm)
        self.medium_btn = Button(w // 2 - 40, h - 155, 80, 40, "Medium", sm)
        self.hard_btn = Button(w // 2 + 80, h - 155, 80, 40, "Hard", sm)

        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)
        self.ui_list.extend(
            [self.exit_button,
             self.number_text, self.ten_button, self.twenty_button, self.thirty_button,
             self.theme_text, self.light_button, self.medium_button, self.dark_button,
             self.mode_text, self.one_game, self.level_up, self.no_error,
             self.difficulty, self.easy_btn, self.medium_btn, self.hard_btn])
        self.max_rounds_options = [self.ten_button, self.twenty_button, self.thirty_button]
        self.themes = [self.light_button, self.medium_button, self.dark_button]
        self.modes = [self.one_game, self.level_up, self.no_error]
        self.difficulties = [self.easy_btn, self.medium_btn, self.hard_btn]

    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event)
            assign_values(event, self) # After options are set values applied after switching back to Menu scene


    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)



