import pygame

from logic.files import process_trivia_file
from scenes.base_scene import *

class GameScene(BaseScene):
    def __init__(self, sm):
        super().__init__(sm)
        w = sm.screen.get_width()
        h = sm.screen.get_height()

        self.addition = "" # Addition to text when Level up mode is active
        self.questions = process_trivia_file(self.scene_manager.filename) # List of questions initializer
        self.selected = update_question(self.questions) # random question selected, with shuffled answers
        if sm.mode_value == 'Level up':
            sm.max_questions = 10 # Level up mode can only have 10 questions each level
            self.addition = f"/{sm.correct_to_level_up}" # Addition gets value

        # Creating UI elements
        self.correct_answers_text = Text(w // 2 + 250, h - 560, 0, 0, sm,
                                         f"Correct answers: {sm.correct_count}{self.addition}", 30)
        self.timer_text = Text(w // 2, h - 560, 0, 0, sm, str(sm.time_left))
        self.question_count_text = Text(w // 2 - 250, h - 560, 0, 0, sm,
                                        f"Question: {sm.question_count}/{sm.max_questions}", 30)
        self.question_text = Text(w // 2, h - 420, 0, 0, sm, self.selected.question, 30)

        self.answer_one_button = Button(w // 2 - 200, h - 400, 400, 40, self.selected.answers[0], sm)
        self.answer_two_button = Button(w // 2 - 200, h - 340, 400, 40, self.selected.answers[1], sm)
        self.answer_three_button = Button(w // 2 - 200, h - 280, 400, 40, self.selected.answers[2], sm)
        self.next_button = Button(w // 2 - 40, h - 130, 80, 40, "Next", sm, False, False)
        self.exit_button = Button(w // 2 - 40, h - 80, 80, 40, "Exit", sm)

        self.ui_list.extend([self.question_text, self.answer_one_button, self.answer_two_button, self.answer_three_button,
             self.next_button, self.exit_button, self.correct_answers_text, self.question_count_text, self.timer_text])
        self.answers_list = [self.answer_one_button, self.answer_two_button, self.answer_three_button]
        self.is_chosen = False

    def start(self):
        if self.scene_manager.mode_value == 'No error': # Hide questions count when No error mode active
            self.question_count_text.visible = False

    def update_scene(self):
        super().update_scene()
        if not self.is_chosen:
            self.scene_manager.countdown_timer() # Countdown only if not answered
        if self.scene_manager.time_left <= 0: # When time expire
            self.timer_text.update_text('0') # Set text to 0
            for button in self.answers_list: button.active = False # Set all buttons not active
            self.scene_manager.is_correct = False # is_correct to False as well
            # Go to game over scene if is it No error mode
            if not self.scene_manager.is_correct and self.scene_manager.mode_value == 'No error':
                self.scene_manager.restart_game(self.scene_manager.game_over_scene)
            self.next_button.active = True
            self.next_button.visible = True
        for event in self.scene_manager.events:
            if event.type == pygame.KEYDOWN: # Checking for keyboard action
                if event.key == pygame.K_t:
                    self.scene_manager.time_left = 6
                if event.key == pygame.K_ESCAPE: # If escape button is clicked go to pause menu
                    self.scene_manager.switch_scene(self.scene_manager.pause_scene)
                if event.key == pygame.K_SPACE and self.next_button.active: # Move to next question using space key
                    self.next_question()
            if self.next_button.is_clicked(event, self.scene_manager.sounds['click']):
                self.next_question() # Move to next question by clicking on Next button
            self.scene_manager.is_correct = check_answer(self, event) # Return bool value for is_correct
            self.exit_scene(event)


    def exit_scene(self, event):
        exit_handlers = { # Declaring dict with Keys and Values to handle exit condition for each game mode
            'One game': lambda: self.one_game_exit(),
            'Level up': lambda: self.level_up_exit(),
            'No error': lambda: self.no_error_exit()
        }
        if self.exit_button.is_clicked(event, self.scene_manager.sounds['click']):
            self.scene_manager.restart_game(self.scene_manager.menu_scene) # Go back to menu scene if exit is clicked
            self.scene_manager.correct_to_level_up = 4 # Set values back to initial
            self.scene_manager.player.score = 0 # Same for plyer score
        exit_handlers[self.scene_manager.mode_value]()

    def next_question(self):
        # Reset all relevant values
        self.is_chosen = False
        self.next_button.active = False
        self.next_button.visible = False
        self.questions.remove(self.selected) # Remove question from the list not to repeat it
        self.selected = update_question(self.questions) # Chose new one
        question_view(self.selected, self) # Set new view for question
        update_view(self) # Update the view and set all graphics to inintial
        self.scene_manager.time_left = 30 # Reset timer back
        [setattr(button, 'active', True)for button in self.answers_list] # Make buttons active again

    # One game mode exit condition
    def one_game_exit(self):
        if end_game(self.scene_manager):
            self.scene_manager.restart_game(self.scene_manager.game_over_scene)

    # Level up mode exit condition
    def level_up_exit(self):
        if end_game(self.scene_manager):
            # If level passed
            if self.scene_manager.check_level_up() and self.scene_manager.correct_to_level_up < self.scene_manager.max_questions:
                self.scene_manager.correct_to_level_up += 2
                self.scene_manager.restart_game(self.scene_manager.game_scene)
            else: # If level not passed
                self.scene_manager.restart_game(self.scene_manager.game_over_scene)

    # No error mode exit condition
    def no_error_exit(self):
        if not self.scene_manager.is_correct:
            self.scene_manager.restart_game(self.scene_manager.game_over_scene)
