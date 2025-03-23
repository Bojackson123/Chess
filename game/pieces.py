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

def flip_threat_maps(w_matrix, b_matrix):
    w_matrix[0][3], w_matrix[7][4] = w_matrix[7][4], w_matrix[0][3]
    b_matrix[0][4], b_matrix[7][3] = b_matrix[7][3], b_matrix[0][4]
    return w_matrix, b_matrix


class Pieces:
    def __init__(self, color):
        self.board = generate_board()
        self.white_images =  WHITE_IMAGES
        self.black_images = BLACK_IMAGES
        self.color = color
        self.white_threat_map = [[0, 0, 0, 3, 0, 0, 0, 0],  # threat map for whites king
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.black_threat_map = [[0, 0, 0, 0, 0, 0, 0, 0],  # threat map for blacks king
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 3, 0, 0, 0, 0]]
        self.white_possible_moves = []
        self.black_possible_moves = []
        self.black_pawn_moved = [0, 0, 0, 0, 0, 0, 0, 0] # boolean array for black pawns first moves
        self.white_pawn_moved = [0, 0, 0, 0, 0, 0, 0, 0] # boolean array for white pawns first moves
        
        
        if self.color == "white":
            self.board = flip_board_coords(self.board)
            self.white_threat_map, self.black_threat_map = flip_threat_maps(self.white_threat_map, self.black_threat_map)
    
    
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
    
    def has_piece(self, mouse_pos):
        for key, value in self.board.items():
            piece_x, piece_y = value[2]
            piece_rect = pygame.Rect(piece_x, piece_y, 100, 100)
            
            if piece_rect.collidepoint(mouse_pos):
                if value[0] != None:
                    return True
                else:
                    return False
                
        return False
    
    def is_in_bounds(self, coords):
        x, y = coords
        if 0 <= x <= 7 and 0 <= y <= 7:
            return True
        else:
            return False 
    
    def pawn_possible_moves(self, color, coords):# (2, 6)
        x, y = coords
        possible_moves = []
        if self.color == "black":
            if color == "black":
                possible_moves.append((x, y - 1))
                possible_moves.append((x - 1, y - 1))
                possible_moves.append((x + 1, y - 1))
                if self.black_pawn_moved[y] == 0:
                    possible_moves.append((x, y - 2))
            else:
                possible_moves.append((x, y + 1))
                possible_moves.append((x - 1, y + 1))
                possible_moves.append((x + 1, y + 1))
                if self.white_pawn_moved[y] == 0:
                    possible_moves.append((x, y + 2))
        
        else:
            if color == "black":
                possible_moves.append((x, y + 1))
                possible_moves.append((x - 1, y + 1))
                possible_moves.append((x + 1, y + 1))
                if self.black_pawn_moved[y] == 0:
                    possible_moves.append((x , y + 2))
            else:
                possible_moves.append((x, y - 1))
                possible_moves.append((x - 1, y - 1))
                possible_moves.append((x + 1, y - 1))
                if self.white_pawn_moved[y] == 0:
                    possible_moves.append((x , y - 2))
        
        inbound_moves = []
        for move in possible_moves:
            if self.is_in_bounds(move):
                inbound_moves.append(move)
        return inbound_moves  
            
    
    def rook_possible_moves(self, coords):
        x, y = coords
        possible_moves = []
        moves = ["up", "down", "left", "right" ]
        
        for move in moves:
            if move == "up":
                j = y - 1
                while j >= 0:
                    possible_moves.append((x, j))
                    j -= 1
            
            if move == "down":
                j = y + 1
                while j <= 7:
                    possible_moves.append((x, j))
                    j += 1
            
            if move == "left":
                j = x - 1
                while j >= 0:
                    possible_moves.append((j, y))
                    j -= 1
            
            if move == "right":
                j = x + 1
                while j <= 7:
                    possible_moves.append((j, y))
                    j += 1
        
        return possible_moves        
    
    def knight_possible_moves(self, color, coords):
        pass
    
    def bishop_possible_moves(self, color, coords):
        pass
    
    def queen_possible_moves(self, color, coords):
        pass
    
    def king_possible_moves(self, color, coords):
        pass
    
    
                
        
    