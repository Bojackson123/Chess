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
        self.turn = self.color
        self.selected_piece = None
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
    
    def get_turn(self):
        return self.turn
    
    def set_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
    
    def is_piece_selected(self):
        return True if self.selected_piece else False
    
    def select_piece(self, mouse_pos):
        for key, value in self.board.items():
            x, y = value[2]
            piece_rect = pygame.Rect(x, y, 100, 100)
            
            if piece_rect.collidepoint(mouse_pos):
                if value[0] != None:
                    self.selected_piece = key
                    
    def deselect_piece(self):
        self.selected_piece = None
    
    def is_turns_piece(self):
        if self.board[self.selected_piece][1] == self.turn:
            return True
        else:
            return False
      
    def move_piece(self, mouse_pos):
        curr_piece = self.board[self.selected_piece]
        for key, value in self.board.items():
            x, y = value[2] 
            piece_rect = pygame.Rect(x, y, 100, 100)
            if piece_rect.collidepoint(mouse_pos):
                print(f'Value: {value[1]}')
                print(f'Turn: {self.turn}')
                value[0] = curr_piece[0]
                value[1] = curr_piece[1]
                self.board[self.selected_piece][0] = None
                self.board[self.selected_piece][1] = None
            
        self.deselect_piece()
        self.set_turn()
    
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
    
    def pawn_legal_moves(self, coords):
        if coords is None:
            return
        
        x, y = coords
        legal_moves = []

        piece, color, _ = self.board[coords]
        direction = 1 if color == "white" else -1  # White moves up (y+1), black moves down (y-1)
        start_row = 1 if color == "white" else 6
        promotion_row = 7 if color == "white" else 0

        # Normal 1-square move forward
        if (x, y + direction) in self.board and self.board[(x, y + direction)][0] is None:
            legal_moves.append((x, y + direction))

            # Double move from starting position
            if y == start_row and (x, y + 2 * direction) in self.board and self.board[(x, y + 2 * direction)][0] is None:
                legal_moves.append((x, y + 2 * direction))

        # Capture diagonally (left and right)
        for dx in [-1, 1]:
            nx, ny = x + dx, y + direction
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) in self.board:
                    target_piece, target_color, _ = self.board[(nx, ny)]
                    if target_piece is not None and target_color != color:
                        legal_moves.append((nx, ny))

        return legal_moves
  
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
    
    def rook_legal_moves(self, coords):
        if coords is None:
            return
        x, y = coords
        legal_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Keep moving in one direction until blocked or off-board
            while 0 <= nx < 8 and 0 <= ny < 8:  # Ensure within the 8x8 grid
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]
                    
                    # If the square is empty (None), it's a legal move
                    if piece is None:
                        legal_moves.append((nx, ny))
                    else:
                        # If the square contains an opponent piece, it's a capture move
                        if color != self.board[(x, y)][1]:
                            legal_moves.append((nx, ny))
                        break  # Stop moving after any piece (friend or enemy)
                else:
                    # Just in case any square isn’t in the board dictionary
                    legal_moves.append((nx, ny))

                # Move further in the current direction
                nx += dx
                ny += dy

        return legal_moves

    def knight_possible_moves(self, coords):# (2, 5)
        x, y = coords
        possible_moves = []
        
        possible_moves.append((x - 2, y - 1))
        possible_moves.append((x - 1, y - 2))
        
        possible_moves.append((x + 1, y - 2))
        possible_moves.append((x + 2, y - 1))
        
        possible_moves.append((x + 2, y + 1))
        possible_moves.append((x + 1, y + 2))
        
        possible_moves.append((x - 1, y + 2))
        possible_moves.append((x - 2, y + 1))
        
        inbound_moves = []
        for move in possible_moves:
            if self.is_in_bounds(move):
                inbound_moves.append(move)
        
        return inbound_moves
    
    def knight_legal_moves(self, coords):
        if coords is None:
            return
        
        x, y = coords
        legal_moves = []

        # All possible "L" shape moves for a knight
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Ensure the move stays within the 8x8 board
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]

                    # Either the square is empty or has an opponent piece (capture)
                    if piece is None or color != self.board[(x, y)][1]:
                        legal_moves.append((nx, ny))

        return legal_moves
   
    def bishop_possible_moves(self, coords):
        x, y = coords
        possible_moves = []
        moves = ["top-left", "top-right", "bot-left", "bot-right"]
        
        for move in moves:
            if move == "top-left":
                i, j = x - 1, y - 1
                while i >= 0 and j >= 0:
                    possible_moves.append((i, j))
                    i -= 1
                    j -= 1
            
            if move == "top-right":
                i, j = x + 1, y - 1
                while i <= 7 and j >= 0:
                    possible_moves.append((i, j))
                    i += 1
                    j -= 1
            
            if move == "bot-left":
                i, j = x - 1, y + 1
                while i >= 0 and j <= 7:
                    possible_moves.append((i, j))
                    i -= 1
                    j += 1
            
            if move == "bot-right":
                i, j = x + 1, y + 1
                while i <= 7 and j <= 7:
                    possible_moves.append((i, j))
                    i += 1
                    j += 1
        
        return possible_moves
    
    def bishop_legal_moves(self, coords):
        if coords is None:
            return
        x, y = coords
        legal_moves = []
        directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)]  # Top-Right, Top-Left, Bot-Right, Bot-Left

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Keep moving in one direction until blocked or off-board
            while 0 <= nx < 8 and 0 <= ny < 8:  # Ensure within the 8x8 grid
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]
                    
                    # If the square is empty (None), it's a legal move
                    if piece is None:
                        legal_moves.append((nx, ny))
                    else:
                        # If the square contains an opponent piece, it's a capture move
                        if color != self.board[(x, y)][1]:
                            legal_moves.append((nx, ny))
                        break  # Stop moving after any piece (friend or enemy)
                else:
                    # Just in case any square isn’t in the board dictionary
                    legal_moves.append((nx, ny))

                # Move further in the current direction
                nx += dx
                ny += dy

        return legal_moves
    
    def queen_possible_moves(self, coords):
        possible_moves = self.bishop_possible_moves(coords) + self.rook_possible_moves(coords)
        
        return possible_moves
    
    def queen_legal_moves(self, coords):
        if coords is None:
            return
        legal_moves = self.bishop_legal_moves(coords) + self.rook_legal_moves(coords)
        return legal_moves
    
    def king_possible_moves(self, coords):
        x, y = coords
        possible_moves = []
        
        possible_moves.append((x - 1, y - 1))
        possible_moves.append((x, y - 1))
        possible_moves.append((x + 1, y - 1))
        possible_moves.append((x + 1, y))
        possible_moves.append((x + 1, y + 1))
        possible_moves.append((x, y + 1))
        possible_moves.append((x - 1, y + 1))
        possible_moves.append((x - 1, y))

        inbound_moves = []
        for move in possible_moves:
            if self.is_in_bounds(move):
                inbound_moves.append(move)
                
        return inbound_moves
    
    def king_legal_moves(self, coords):
        if coords is None:
            return
        
        x, y = coords
        legal_moves = []

        # King moves one square in any direction
        moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal directions
        ]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Ensure move stays within the board
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]

                    # If square is empty or has an opponent's piece (capture)
                    if piece is None or color != self.board[(x, y)][1]:
                        legal_moves.append((nx, ny))

        return legal_moves

                
        
    