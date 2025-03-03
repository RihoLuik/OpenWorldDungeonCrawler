import pygame
import sys
from utils import Button, WHITE, get_screen_resolution, get_scale_factor

# Initialize pygame
def run_settings(previous_screen):
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
    screen = previous_screen # Keep the same screen

    scale_factor = get_scale_factor()
    buttons = []

    def update_ui():
        """Recalculates UI elements when the window resizes."""
        nonlocal buttons, scale_factor

        button_width = int(700 * scale_factor)
        button_height = int(100 * scale_factor)
        button_x = int(600 * scale_factor)

        buttons = [
            Button("Toggle Window Mode", button_x, int(270 * scale_factor), button_width, button_height,
                   toggle_window_mode),
            Button("Increase Volume", button_x, int(430 * scale_factor), button_width, button_height,
                   lambda: change_volume(True)),
            Button("Decrease Volume", button_x, int(590 * scale_factor), button_width, button_height,
                   lambda: change_volume(False)),
            Button("Back", button_x, int(750 * scale_factor), button_width, button_height, back_to_main),
        ]

    # Store the window mode
    window_modes = ["Windowed", "Fullscreen"]
    current_mode_index = 0
    volume = 1.0

    # Toggle Window Mode
    def toggle_window_mode():
        nonlocal current_mode_index, screen, SCREEN_WIDTH, SCREEN_HEIGHT
        current_mode_index = (current_mode_index + 1) % len(window_modes)
        mode = window_modes[current_mode_index]

        if mode == "Fullscreen":
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            # **Fix: Reset Windowed Mode to Default Resolution**
            default_width, default_height = 1280, 720  # Change this if needed
            screen = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)

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

    # Initialize UI elements
    update_ui()

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
                update_ui()  # **Recalculate UI elements when resized**

            for button in buttons:
                if button.check_click(event) is False:
                    running = False

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()