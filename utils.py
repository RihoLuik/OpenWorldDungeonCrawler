import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
HOVER_COLOR = (200, 200, 200)

# Get Screen Resolution
def get_screen_resolution():
    info = pygame.display.Info()
    return info.current_w, info.current_h

# Scaling Function
def get_scale_factor(base_width=1920, base_height=1080):
    screen_width, screen_height = get_screen_resolution()
    scale_x = screen_width / base_width
    scale_y = screen_height / base_height
    return min(scale_x, scale_y) # Keep uniform scaling

# Get Scaled Font
def get_font(size):
    scale_factor = get_scale_factor()
    return pygame.font.Font(None, int(size * scale_factor))

# Button Class
class Button:
    def __init__(self, text, x, y, width, height, action=None):
        scale_factor = get_scale_factor()
        self.text = text
        self.rect = pygame.Rect(
            int(x * scale_factor),
            int(y * scale_factor),
            int(width * scale_factor),
            int(height * scale_factor),
        )
        self.action = action
        self.font = get_font(50)

    def draw(self, surface):
        color = HOVER_COLOR if self.rect.collidepoint(pygame.mouse.get_pos()) else GRAY
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 3)

        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                return self.action()