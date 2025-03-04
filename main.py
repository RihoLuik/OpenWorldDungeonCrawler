import pygame
import sys
from utils import Button, WHITE, get_screen_resolution, get_scale_factor

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dungeon Crawler - Menu")

def force_refresh():
    """Clears the screen, redraws all elements, and updates display."""
    screen.fill(WHITE)  # Clear screen
    for button in buttons:
        button.draw(screen)  # Redraw buttons
    pygame.display.flip()  # 🔥 FORCE DISPLAY UPDATE

# Function to update buttons dynamically
def update_buttons():
    global buttons, SCREEN_WIDTH, SCREEN_HEIGHT, screen

    # Get the latest screen resolution
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    scale_factor = get_scale_factor()

    # Calculate button dimensions
    button_width = int(700 * scale_factor)
    button_height = int(100 * scale_factor)

    # 🔥 Corrected Centering Formula (This WILL fix the issue)
    button_x = (SCREEN_WIDTH - button_width) // 2
    start_y = (SCREEN_HEIGHT - (2 * button_height + 50)) // 2

    gap = int(150 * scale_factor)

    # Debugging: Check positioning calculations
    print(f"Updated Screen Size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Button Size: {button_width}x{button_height}")
    print(f"Corrected X Position: {button_x}, Expected Center: {SCREEN_WIDTH // 2}")

    # Recreate buttons with the fixed positions
    buttons = [
        Button("Start Game", button_x, start_y, button_width, button_height, start_game),
        Button("Quit", button_x, start_y + gap, button_width, button_height, quit_game),
    ]

    force_refresh()  # 🔥 Ensure screen updates correctly

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
    screen.fill(WHITE)  # Always clear screen before drawing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

            update_buttons()  # Recalculate positions
            force_refresh()  # 🔥 Force redraw

        for button in buttons:
            button.check_click(event)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()  # 🔥 Make sure display updates every frame

pygame.quit()
sys.exit()