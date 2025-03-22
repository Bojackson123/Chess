import pygame
from .constants import GREEN, WHITE

class Board():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.tile_size = 100
        self.tiles = []  # Matrix to hold each tile's rectangle and color
        
        color1 = WHITE
        color2 = GREEN
        
        # Populate the matrix with rectangles and colors
        for row in range(0, self.height // self.tile_size):
            row_tiles = []
            for col in range(0, self.width // self.tile_size):
                color = color1 if (row + col) % 2 == 0 else color2
                rect = pygame.Rect(
                    col * self.tile_size, 
                    row * self.tile_size, 
                    self.tile_size, 
                    self.tile_size
                )
                row_tiles.append({'rect': rect, 'color': color})
            self.tiles.append(row_tiles)

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background
        
        # Draw each tile from the matrix
        for row in self.tiles:
            for tile in row:
                pygame.draw.rect(screen, tile['color'], tile['rect'])
