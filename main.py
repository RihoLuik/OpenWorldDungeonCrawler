import pygame
import sys
import settings # Import settings.py
from utils import Button, WHITE, get_screen_resolution, get_scale_factor

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dungeon Crawler - Menu")

# Scaling factor
scale_factor = get_scale_factor()

# Button actions
def start_game():
    print("Starting Game...") # Placeholder

def open_settings():
    settings.run_settings(screen)

def quit_game():
    pygame.quit()
    sys.exit()

# Create buttons
buttons = [
    Button("Start Game", 600, 270, 700, 100, start_game),
    Button("Settings", 600, 430, 700, 100, open_settings),
    Button("Quit", 600, 590, 700, 100, quit_game),
]

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        for button in buttons:
            button.check_click(event)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()