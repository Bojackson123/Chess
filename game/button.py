import pygame
from game import SCREEN_HEIGHT, SCREEN_WIDTH, FONT


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Button Class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, font, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)  # Button rectangle
        self.text = text  # Button label text
        self.color = color  # Normal button color
        self.hover_color = hover_color  # Hover button color
        self.font = font  # Font for the button text
        self.text_color = text_color  # Color for the button text
        self.current_color = color  # Current color of the button (changes on hover)

    def draw(self, screen):
        # Draw button rectangle
        pygame.draw.rect(screen, self.current_color, self.rect)
        # Render and draw the text on the button
        text_surf = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
                                self.rect.y + (self.rect.height - text_surf.get_height()) // 2))

    def is_hovered(self, mouse_pos):
        # Check if the mouse is over the button
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        # Check if the button was clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click
            return self.is_hovered(pygame.mouse.get_pos())
        return False

    def update(self, mouse_pos):
        # Update button color based on hover state
        is_hovering = self.is_hovered(mouse_pos)
        self.current_color = self.hover_color if is_hovering else self.color
        return is_hovering  # Return whether the button is hovered