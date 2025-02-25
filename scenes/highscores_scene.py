from logic.files import read_scores
from scenes.base_scene import *


class HighscoresScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)
        self.title_text = Text(w // 2, h // 2 - 120, 0, 0, sm, "Top 10", 50)
        self.ui_list.extend([self.exit_button, self.title_text])


    def start(self):
        # Get 10 scores decreasing
        highscores = sorted(read_scores('files/scores.db'), key=lambda x: int(x[1]), reverse=True)[:10]
        offset = 0
        # Print it on the screen with format names left lined up, scores right lined up
        for place, data in enumerate(highscores, start=1):
            player_name = Text(self.scene_manager.screen.get_width() // 2 - 30,
                               self.scene_manager.screen.get_height() // 2 - 60 + offset,
                               0, 25, self.scene_manager, f"{place}. {data[0]}")
            player_name.rect = player_name.surface.get_rect(bottomleft=(player_name.x - 70, player_name.y))
            player_score = Text(self.scene_manager.screen.get_width() // 2 - 30,
                                self.scene_manager.screen.get_height() // 2 - 80 + offset,
                                0, 25, self.scene_manager, f"{data[1]}")
            player_score.rect = player_score.surface.get_rect(bottomleft=(player_score.x + 120, player_score.y + 20))
            self.ui_list.extend([player_name, player_score])
            offset += 25 # Move it to next row

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event)

    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)
