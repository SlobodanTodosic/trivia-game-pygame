from scenes.scene_manager import *

WIDTH, HEIGHT = 960, 600

pygame.init() # Initializing pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Setting display size
pygame.display.set_caption("TRIVIA GAME")
scene_manager = SceneManager(screen) # Initializing scene manager
scene_manager.start() # Starting it

current_scene = scene_manager.get_current_scene() # Getting the current scene

running = True
while running:
    scene_manager.set_events(pygame.event.get()) # Setting all the events of pygame
    for event in scene_manager.events:
        if event.type == pygame.QUIT:
            running = False

    scene_manager.update() # Update scene manager in game loop
    pygame.display.update() # Refresh screen every frame

pygame.quit() # Quit if quit condition is met
