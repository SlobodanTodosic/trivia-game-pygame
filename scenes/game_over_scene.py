from logic.files import save_score
from scenes.base_scene import *

class GameOverScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.exit_button = Button(w // 2 - 40, h - 80,80, 40, "Exit", sm)
        self.game_over_text = Text(w // 2, h // 2 - 80, 0, 0, sm, "GAME OVER", 50)
        self.score_text = Text(w // 2, h // 2, 0, 0, sm,
                               f"{sm.player.name} won {sm.player.score} points!")
        sm.correct_to_level_up = 4
        sm.is_correct = True
        sm.time_left = 30
        self.ui_list.extend([self.exit_button, self.score_text, self.game_over_text])

    def start(self):
        save_score(self.scene_manager.player, 'files/scores.db') # At start save scores to database
        self.scene_manager.player.score = 0 # Set player score back to 0

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event) # Waiting for the exit condition

    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)