import pygame
from .constants import WHITE_LOCATIONS, WHITE_PIECES, BLACK_LOCATIONS, BLACK_PIECES, BLACK_IMAGES, WHITE_IMAGES

def generate_board():
    board_dict = {}
    x = 0
    y = 0
    for i in range(8):
        for j in range(8):
            board_dict[(j, i)] = [None, None, (x, y)]
            x += 100
        y += 100
        x = 0
    
    for i in range(16):
        board_dict[WHITE_LOCATIONS[i]][0] = WHITE_PIECES[i]
        board_dict[WHITE_LOCATIONS[i]][1] = "white"
        board_dict[BLACK_LOCATIONS[i]][0] = BLACK_PIECES[i]
        board_dict[BLACK_LOCATIONS[i]][1] = "black"
    return board_dict

def flip_board_coords(board_dict):
    flipped_board = {}
    for (x, y), data in board_dict.items():
        piece, color, (px, py) = data
        # Flip grid coordinates
        new_coords = (7 - x, 7 - y)
        # Flip pixel positions
        new_pixel_pos = (700 - px, 700 - py)
        # Update the flipped board state
        flipped_board[new_coords] = [piece, color, new_pixel_pos]
    return flipped_board


class Pieces:
    def __init__(self, color):
        self.board = generate_board()
        self.white_images =  WHITE_IMAGES
        self.black_images = BLACK_IMAGES
        self.color = color

        if self.color == "white":
            self.board = flip_board_coords(self.board)
    
    
    def draw_pieces(self, screen):
        for key, value in self.board.items():
            if value[1] == "white":
                if value[0] == "rook":
                    screen.blit(self.white_images["rook"], value[2])
                    continue
                
                if value[0] == "knight":
                    screen.blit(self.white_images["knight"], value[2])
                    continue
                
                if value[0] == "bishop":
                    screen.blit(self.white_images["bishop"], value[2])
                    continue
                
                if value[0] == "king":
                    screen.blit(self.white_images["king"], value[2])
                    continue
                
                if value[0] == "queen":
                    screen.blit(self.white_images["queen"], value[2])
                    continue
                
                if value[0] == "pawn":
                    screen.blit(self.white_images["pawn"], value[2])
                    continue
            
                    
            elif value[1] == "black":
                if value[0] == "rook":
                    screen.blit(self.black_images["rook"], value[2])
                    continue
                
                if value[0] == "knight":
                    screen.blit(self.black_images["knight"], value[2])
                    continue
                
                if value[0] == "bishop":
                    screen.blit(self.black_images["bishop"], value[2])
                    continue
                
                if value[0] == "king":
                    screen.blit(self.black_images["king"], value[2])
                    continue
                
                if value[0] == "queen":
                    screen.blit(self.black_images["queen"], value[2])
                    continue
                
                if value[0] == "pawn":
                    screen.blit(self.black_images["pawn"], value[2])
                    continue
            
                
        
    