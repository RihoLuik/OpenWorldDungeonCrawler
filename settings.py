import pygame
import sys
from utils import Button, WHITE, get_screen_resolution, get_scale_factor

# Initialize pygame
def run_settings(previous_screen):
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
    screen = previous_screen # Keep the same screen
    scale_factor = get_scale_factor()

    # Store the window mode
    window_modes = ["Windowed", "Fullscreen", "Borderless"]
    current_mode_index = 0

    volume = 1.0

    # Toggle Window Mode
    def toggle_window_mode():
        nonlocal current_mode_index, screen, SCREEN_WIDTH, SCREEN_HEIGHT
        current_mode_index = (current_mode_index + 1) % len(window_modes)
        mode = window_modes[current_mode_index]

        if mode == "Fullscreen":
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        elif mode == "Borderless":
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
        else:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        pygame.display.flip()  # Force update
        print(f"Window Mode: {mode}")

    # Adjust Volume (Placeholder for actual sound system)
    def change_volume(increase=True):
        nonlocal volume
        step = 0.1
        volume = min(1.0, max(0.0, volume + (step if increase else -step)))
        print(f"Volume: {int(volume * 100)}%")

    # Back to Main Menu
    def back_to_main():
        return False # This will signal the loop to exit

    # Create Scaled Buttons
    buttons = [
        Button("Toggle Window Mode", 600, 270, 700, 100, toggle_window_mode),
        Button("Increase Volume", 600, 430, 700, 100, lambda: change_volume(True)),
        Button("Decrease Volume", 600, 590, 700, 100, lambda: change_volume(False)),
        Button("Back", 600, 750, 700, 100, back_to_main),
    ]

    # Settings Loop
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

            for button in buttons:
                if button.check_click(event) is False:
                    running = False

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()