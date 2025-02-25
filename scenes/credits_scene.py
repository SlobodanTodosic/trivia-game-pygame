from scenes.base_scene import *

class CreditsScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()
        # Creating UI elements
        self.exam_text = Text(w // 2, h // 2 - 80, 0, 0, sm, "CS324 Skripting jezici", 50)
        self.student_name_text = Text(w // 2, h // 2 - 30, 0, 0, sm, "Slobodan Todosić, 4653")
        self.professor_name_text = Text(w // 2, h // 2 + 80, 0, 0, sm, "Profesor: Nemanja Zdravković")
        self.assistant_name_text = Text(w // 2, h // 2 + 120, 0, 0, sm, "Asistent: Tamara Vukadinović")
        self.school_name_text = Text(w // 2, h // 2 + 160, 0, 0, sm,
                                     "Metropolitan Univerzitet, Beograd 2024/2025")
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", self.scene_manager)

        self.ui_list.extend([self.exit_button, self.exam_text, self.student_name_text,
                             self.professor_name_text, self.assistant_name_text, self.school_name_text])

    def start(self):
        pass

    def update_scene(self):
        super().update_scene()
        for event in self.scene_manager.events:
            self.exit_scene(event) # Waiting for exit condition

    def exit_scene(self, event):
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.switch_scene(self.scene_manager.menu_scene)
