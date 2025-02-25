import random

import pygame

# Random question selected from list of Question objects
def pick_random_question(questions):
    selected_question = random.choice(questions)
    return selected_question

# Function to get portion of the image strip, to create animation
def get_image(sheet, width, height, current_frame=0):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (current_frame * width, 0, width, height)) # Blit the selection to image surface
    return image

# region OPTIONS_LOGIC
# Function to return text of a button clicked
def clicked_options(event, buttons, scene):
    # Finding clicked button
    clicked_element = next((e for e in buttons if e.is_clicked(event, scene.scene_manager.sounds['click'])), None)
    if clicked_element:
        [b.set_visual_hover('80') for b in buttons] # Setting the buttons to original base and hover colors
        clicked_element.set_visual_no_hover('s80') # Setting color for clicked button
        return clicked_element.text


def assign_values(event, options_scene):
    mapping = { # Dict of option names and variables to change, and values to assign
        "max_rounds_options": ('max_questions', int),
        "themes": ('theme_value', str),
        "modes": ('mode_value', str),
        "difficulties": ('filename', lambda x: f"files/{x.lower()}.txt")
    }

    for option_name, (attribute, action) in mapping.items(): # For loop with option name, and attribute and action in all dict items
        option = getattr(options_scene, option_name) # Option gets the value of option_name
        value = clicked_options(event, option, options_scene) # value is assigned text of clicked button
        if value:
            value = action(value) # Formating value to format needed
            setattr(options_scene.scene_manager, attribute, value) # Setting scene manager attribute with selected value
# endregion

# region GAME_LOGIC
# Function to check clicked answer
def check_answer(game_scene, event):
    # Getting the clicked button and assigning it to chosen answer
    chosen_answer = next((answer for answer in game_scene.answers_list if answer.is_clicked(event, game_scene.scene_manager.sounds['click'])), None)
    if chosen_answer:
        game_scene.is_chosen = True # Making var is_chosen to True for future use
        # Make Next button visible
        game_scene.next_button.active = True
        game_scene.next_button.visible = True
        is_correct = chosen_answer.text == game_scene.selected.correct_answer # Check if answer is correct

        chosen_answer.set_visual_no_hover('c400' if is_correct else 'w400') # Changing button color to red or green if wrong or correct
        game_scene.scene_manager.correct_count += 1 if is_correct else 0 # Increase score if answer correct
        # Play sound if wrong or correct
        game_scene.scene_manager.sounds['correct'].play() if is_correct else game_scene.scene_manager.sounds['error'].play()
        # Update text to correct score
        game_scene.correct_answers_text.update_text(f"Correct answers: {game_scene.scene_manager.correct_count}"
                                                    f"{game_scene.addition}")
        # Showing correct answer
        correct_answer = next(btn for btn in game_scene.answers_list if btn.text == game_scene.selected.correct_answer)
        correct_answer.set_visual_no_hover('c400')
        # Set buttons inactive to prevent clicks after the question is answered
        [setattr(button, 'active', False)for button in game_scene.answers_list]

        return is_correct
    return True
# Function to update question with Next button clicked
def update_question(questions):
    question = pick_random_question(questions)
    random.shuffle(question.answers) # Randomly set A, B and C answer by shuffling them
    return question

# Updating text to show how many questions answered and how many are there to answer
def update_view(game_scene):
    game_scene.scene_manager.question_count += 1
    game_scene.question_count_text.update_text(
        f"Question: {game_scene.scene_manager.question_count}/{game_scene.scene_manager.max_questions}")

def question_view(question, game_scene):
    game_scene.question_text.update_text(question.question) # Updating question text
    for button, new_text in zip(game_scene.answers_list, question.answers): # Combine buttons and answers with zip
        button.update_text(new_text)  # Show answers as buttons text
        button.set_visual_hover('400')

def end_game(scene_manager):
    return scene_manager.max_questions < scene_manager.question_count
# endregion
