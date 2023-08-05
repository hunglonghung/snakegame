import pygame
import sys
import random

# Game Variables
GRAVITY = 0.25
BIRD_MOVEMENT = 0
GAME_ACTIVE = True

# Initialize Pygame
pygame.init()

# Set up display
SCREEN = pygame.display.set_mode((576, 1024))

# Set up assets
BIRD_SURFACE = pygame.image.load('/Users/Admin/Desktop/My_workspace/Python/flappybird.png').convert()
BACKGROUND_SURFACE = pygame.image.load('/Users/Admin/Desktop/My_workspace/Python/images.jpeg').convert()
PIPE_SURFACE = pygame.image.load('/Users/Admin/Desktop/My_workspace/Python/pipe_0.png')
BIRD_SURFACE = pygame.transform.scale(BIRD_SURFACE, (50, 50))
BACKGROUND_SURFACE = pygame.transform.scale(BACKGROUND_SURFACE, (400, 800))

PIPE_SURFACE = pygame.transform.scale(PIPE_SURFACE, (200, 300))

# Set up rect for bird and pipe
BIRD_RECT = BIRD_SURFACE.get_rect(center = (100,512))
PIPE_LIST = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
PIPE_HEIGHT = [400, 600, 800]

def create_pipe():
    random_pipe_pos = random.choice(PIPE_HEIGHT)
    bottom_pipe = PIPE_SURFACE.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = PIPE_SURFACE.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            SCREEN.blit(PIPE_SURFACE, pipe)
        else:
            flip_pipe = pygame.transform.flip(PIPE_SURFACE, False, True)
            SCREEN.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if BIRD_RECT.colliderect(pipe):
            return False

    if BIRD_RECT.top <= -100 or BIRD_RECT.bottom >= 900:
        return False

    return True

# Game Loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and GAME_ACTIVE:
                BIRD_MOVEMENT = 0
                BIRD_MOVEMENT -= 12
        if event.type == SPAWNPIPE:
            PIPE_LIST.extend(create_pipe())
            
    SCREEN.blit(BACKGROUND_SURFACE, (0,0))

    if GAME_ACTIVE:
        # Bird
        BIRD_MOVEMENT += GRAVITY
        rotated_bird = BIRD_SURFACE
        BIRD_RECT.centery += BIRD_MOVEMENT
        SCREEN.blit(rotated_bird, BIRD_RECT)
        GAME_ACTIVE = check_collision(PIPE_LIST)

        # Pipes
        PIPE_LIST = move_pipes(PIPE_LIST)
        draw_pipes(PIPE_LIST)

    # Update the display
    pygame.display.update()

    # # Cap the frame rate
    # CLOCK.tick(120)
