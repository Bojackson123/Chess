import pygame
from .constants import GREEN, WHITE, RED, YELLOW, BLACK

class Board():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.tile_size = 100
        self.tiles = []  # Matrix to hold each tile's rectangle and color
        self.piece_chosen = False
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
                row_tiles.append({'rect': rect, 'color': color, 'highlight': None})
            self.tiles.append(row_tiles)

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
    
    def test_draw(self, coords_list, screen):
        if coords_list is None:
            return
        for coords in coords_list:
            y, x = coords
            tile_rect = self.tiles[x][y]['rect']
            center = tile_rect.center
            radius = min(tile_rect.width, tile_rect.height) // 6

            # Create a transparent surface for the circle
            highlight_surface = pygame.Surface((tile_rect.width, tile_rect.height), pygame.SRCALPHA)
            highlight_color = (0, 0, 0, 50)  # Semi-transparent dark circle
            pygame.draw.circle(highlight_surface, highlight_color, (tile_rect.width // 2, tile_rect.height // 2), radius)

            screen.blit(highlight_surface, tile_rect.topleft)

    
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
    
    def remove_all_highlights(self):
        for row in self.tiles:
            for tile in row:
                tile['highlight'] = None
                            
    def highlight_yellow(self, mouse_pos):
        found = False
        for row in self.tiles:
            for tile in row:
                if tile['rect'].collidepoint(mouse_pos):
                    if self.piece_chosen:
                        self.remove_all_highlights()
                    tile['highlight'] = YELLOW
                    self.piece_chosen = True
                    found = True
                    break
            if found:
                return


        
            
        
            
