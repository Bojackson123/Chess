import pygame
from .constants import GREEN, WHITE, RED, YELLOW, BLACK

class Board():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.tile_size = 100
        self.tiles = []  # Matrix to hold each tile's rectangle and color
        self.default_colors = []
        self.piece_chosen = False
        color1 = WHITE
        color2 = GREEN
        
        # Populate the matrix with rectangles and colors
        for row in range(0, self.height // self.tile_size):
            row_tiles = []
            row_colors = []
            for col in range(0, self.width // self.tile_size):
                color = color1 if (row + col) % 2 == 0 else color2
                rect = pygame.Rect(
                    col * self.tile_size, 
                    row * self.tile_size, 
                    self.tile_size, 
                    self.tile_size
                )
                row_tiles.append({'rect': rect, 'color': color, 'highlight': None})
                row_colors.append(color)
            self.tiles.append(row_tiles)
            self.default_colors.append(row_colors)

    def draw(self, screen):
        screen.fill(BLACK) 
        
        for row in self.tiles:
            for tile in row:
                pygame.draw.rect(screen, tile['color'], tile['rect'])
                
                if tile["highlight"] is not None:
                    highlight_surface = pygame.Surface((tile['rect'].width, tile['rect'].height), pygame.SRCALPHA)
                    highlight_color = tile['highlight'][:3] + (150,) 
                    highlight_surface.fill(highlight_color)
                    screen.blit(highlight_surface, tile['rect'].topleft)
    
    
    def set_piece_chosen(self):
        if self.piece_chosen == True:
            self.piece_chosen == False
        else:
            self.piece_chosen == True
    
    def add_remove_highlight(self, click_type, mouse_pos):
        for row in self.tiles:
            for tile in row:
                if tile['rect'].collidepoint(mouse_pos):
                    if click_type == "left":
                        if tile["highlight"] != YELLOW:
                            tile["highlight"] = YELLOW
                        else:
                            tile["highlight"] = None
                        
                    elif click_type == "right":
                        if tile["highlight"] != RED:
                            tile["highlight"] = RED
                        else:
                            tile["highlight"] = None
            
        
            
