import pygame
import sys
from utils import Button, WHITE, get_screen_resolution, get_scale_factor

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dungeon Crawler - Menu")

# Scaling factor
scale_factor = get_scale_factor()

# Function to update buttons dynamically
def update_buttons():
    global buttons
    scale_factor = get_scale_factor()  # Get updated scale factor
    button_width = int(700 * scale_factor)
    button_height = int(100 * scale_factor)

    # **Proper Centering**
    button_x = SCREEN_WIDTH // 2 - button_width // 2  # Center horizontally
    start_y = SCREEN_HEIGHT // 3  # Start at 1/3 of the screen height
    gap = int(150 * scale_factor)  # Space between buttons

    buttons = [
        Button("Start Game", button_x, start_y, button_width, button_height, start_game),
        Button("Quit", button_x, start_y + gap, button_width, button_height, quit_game),
    ]

# Button actions
def start_game():
    print("Starting Game...")  # Placeholder

def quit_game():
    pygame.quit()
    sys.exit()

# Create buttons initially
update_buttons()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update screen size on window resize
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

            # Recalculate scaling and button positions
            update_buttons()

        for button in buttons:
            button.check_click(event)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()