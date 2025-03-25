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
    
    def get_piece_coords(self, mouse_pos):
        for key, value in self.board.items():
            piece_x, piece_y = value[2]
            piece_rect = pygame.Rect(piece_x, piece_y, 100, 100)
            
            if piece_rect.collidepoint(mouse_pos):
                return key
    
    def move_piece(self, mouse_pos):
        curr_piece = self.board[self.selected_piece]

        # Find where the mouse is pointing (target square)
        for key, value in self.board.items():
            x, y = value[2]
            piece_rect = pygame.Rect(x, y, 100, 100)
            if piece_rect.collidepoint(mouse_pos):
                print(f'Value: {value[1]}')
                print(f'Turn: {self.turn}')

                # If there's an enemy piece at the destination, capture it first
                if value[0] is not None and value[1] != self.turn:
                    self.capture_piece(mouse_pos)

                # Move the selected piece to the target square
                self.board[key] = [curr_piece[0], curr_piece[1], (x, y)]

                # Clear the original square
                self.board[self.selected_piece] = [None, None, self.board[self.selected_piece][2]]

        # Deselect and switch turns
        self.deselect_piece()
        self.set_turn()
   
    def capture_piece(self, mouse_pos):
        for key, value in self.board.items():
            piece_x, piece_y = value[2]
            piece_rect = pygame.Rect(piece_x, piece_y, 100, 100)
            if piece_rect.collidepoint(mouse_pos):
                # Set the captured piece to None instead of deleting it
                self.board[key] = [None, None, value[2]]
                break  # Exit the loop once the target is found

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
        cap_moves = []

        piece, color, _ = self.board[coords]
        
        # Determine direction based on self.color (player's perspective)
        if color == self.color:
            direction = -1  # Player's pawns move "up" the board
            start_row = 6
            promotion_row = 0
        else:
            direction = 1  # Opponent's pawns move "down" the board
            start_row = 1
            promotion_row = 7

        # Normal 1-square move forward
        forward = (x, y + direction)
        if forward in self.board and self.board[forward][0] is None:
            legal_moves.append(forward)

            # Double move from starting row
            double_forward = (x, y + 2 * direction)
            if y == start_row and double_forward in self.board and self.board[double_forward][0] is None:
                legal_moves.append(double_forward)

        # Diagonal captures (left and right)
        for dx in [-1, 1]:
            capture_pos = (x + dx, y + direction)
            if capture_pos in self.board:
                target_piece, target_color, _ = self.board[capture_pos]
                if target_piece is not None and target_color != color:
                    legal_moves.append(capture_pos)
                    cap_moves.append(capture_pos)

        return [legal_moves, cap_moves]
 
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
        cap_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
        
        # Flip directions if White starts on the top
        if self.color == 'white':
            directions = [(-dx, -dy) for dx, dy in directions]

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
                            cap_moves.append((nx, ny))
                        break  # Stop moving after any piece (friend or enemy)
                else:
                    # Just in case any square isn’t in the board dictionary
                    legal_moves.append((nx, ny))

                # Move further in the current direction
                nx += dx
                ny += dy

        return [legal_moves, cap_moves]

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
        capturable_moves = []

        # All possible "L" shape moves for a knight
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        # Flip directions if White starts on the top
        if self.color == 'white':
            moves = [(-dx, -dy) for dx, dy in moves]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Ensure the move stays within the 8x8 board
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]

                    # Empty square
                    if piece is None:
                        legal_moves.append((nx, ny))
                    # Opponent's piece
                    elif color != self.board[(x, y)][1]:
                        legal_moves.append((nx, ny))
                        capturable_moves.append((nx, ny))

        return [legal_moves, capturable_moves]

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
        cap_moves = []
        directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)]  # Top-Right, Top-Left, Bot-Right, Bot-Left
        
        # Flip directions if White starts on the top
        if self.color == 'white':
            directions = [(-dx, -dy) for dx, dy in directions]


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
                            cap_moves.append((nx, ny))
                        break  # Stop moving after any piece (friend or enemy)
                else:
                    # Just in case any square isn’t in the board dictionary
                    legal_moves.append((nx, ny))

                # Move further in the current direction
                nx += dx
                ny += dy

        return [legal_moves, cap_moves]
    
    def queen_possible_moves(self, coords):
        possible_moves = self.bishop_possible_moves(coords) + self.rook_possible_moves(coords)
        
        return possible_moves
    
    def queen_legal_moves(self, coords):
        if coords is None:
            return
        legal_moves = self.bishop_legal_moves(coords)[0] + self.rook_legal_moves(coords)[0]
        cap_moves = self.bishop_legal_moves(coords)[1] + self.rook_legal_moves(coords)[1]
        return [legal_moves, cap_moves]
    
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
        capturable_moves = []

        # King moves one square in any direction
        moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal directions
        ]
        
        # Flip directions if White starts on the top
        if self.color == 'white':
            moves = [(-dx, -dy) for dx, dy in moves]


        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Ensure move stays within the board
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) in self.board:
                    piece, color, _ = self.board[(nx, ny)]

                    # Empty square
                    if piece is None:
                        legal_moves.append((nx, ny))
                    # Opponent's piece
                    elif color != self.board[(x, y)][1]:
                        legal_moves.append((nx, ny))
                        capturable_moves.append((nx, ny))

        return [legal_moves, capturable_moves]

    def is_legal_move(self, mouse_pos):
        piece_coords = self.selected_piece
        piece_type = self.board[self.selected_piece][0]
        move_coords = None
        
        for key, value in self.board.items():
            piece_x, piece_y = value[2]
            piece_rect = pygame.Rect(piece_x, piece_y, 100, 100)
            
            if piece_rect.collidepoint(mouse_pos):
                move_coords = key
        
        if piece_type == "rook":
            if move_coords in self.rook_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
        
        if piece_type == "bishop":
            if move_coords in self.bishop_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
        
        if piece_type == "knight":
            if move_coords in self.knight_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
        
        if piece_type == "queen":
            if move_coords in self.queen_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
        
        if piece_type == "king":
            if move_coords in self.king_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
        
        if piece_type == "pawn":
            if move_coords in self.pawn_legal_moves(piece_coords)[0]:
                return True
            else:
                return False
    
    def legal_moves(self, coords):
        if coords is None:
            return []
        piece_coords = self.selected_piece
        piece_type = self.board[self.selected_piece][0]
        
        if piece_type == "rook":
            return self.rook_legal_moves(piece_coords)[0]
        
        if piece_type == "bishop":
            return self.bishop_legal_moves(piece_coords)[0]
        
        if piece_type == "knight":
            return self.knight_legal_moves(piece_coords)[0]
        
        if piece_type == "queen":
            return self.queen_legal_moves(piece_coords)[0]
        
        if piece_type == "king":
            return self.king_legal_moves(piece_coords)[0]
        
        if piece_type == "pawn":
            return self.pawn_legal_moves(piece_coords)[0]
    
    def is_move_capture(self, mouse_pos):
        piece_coords = self.selected_piece
        piece_type = self.board[self.selected_piece][0]
        move_coords = None
        
        for key, value in self.board.items():
            piece_x, piece_y = value[2]
            piece_rect = pygame.Rect(piece_x, piece_y, 100, 100)
            
            if piece_rect.collidepoint(mouse_pos):
                move_coords = key
        
        if piece_type == "rook":
            if move_coords in self.rook_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
        
        if piece_type == "bishop":
            if move_coords in self.bishop_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
        
        if piece_type == "knight":
            if move_coords in self.knight_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
        
        if piece_type == "queen":
            if move_coords in self.queen_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
        
        if piece_type == "king":
            if move_coords in self.king_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
        
        if piece_type == "pawn":
            if move_coords in self.pawn_legal_moves(piece_coords)[1]:
                return True
            else:
                return False
                        
    def capture_moves(self, coords):
        if coords is None:
            return []
        piece_coords = self.selected_piece
        piece_type = self.board[self.selected_piece][0]
        
        if piece_type == "rook":
            return self.rook_legal_moves(piece_coords)[1]
        
        if piece_type == "bishop":
            return self.bishop_legal_moves(piece_coords)[1]
        
        if piece_type == "knight":
            return self.knight_legal_moves(piece_coords)[1]
        
        if piece_type == "queen":
            return self.queen_legal_moves(piece_coords)[1]
        
        if piece_type == "king":
            return self.king_legal_moves(piece_coords)[1]
        
        if piece_type == "pawn":
            return self.pawn_legal_moves(piece_coords)[1]    
    
    def pawn_threat_map(self, coords):
        if coords is None:
            return []

        x, y = coords
        threats = []
        
        piece, color, _ = self.board[coords]

        # Determine direction based on pawn color
        if self.color == "white":
            direction = -1 if color == "white" else 1
        else:
            direction = 1 if color == "white" else -1

        # Pawns threaten diagonally forward (left and right)
        for dx in [-1, 1]:
            threat_pos = (x + dx, y + direction)
            if 0 <= threat_pos[0] < 8 and 0 <= threat_pos[1] < 8:  # Ensure within bounds
                threats.append(threat_pos)

        return threats

    
    def generate_threat_map(self, color):
        all_legal_moves = []
        
        for key, value in self.board.items():
            if value[1] != color:
                
                piece_coords = key
                piece_type = value[0]
                
                if piece_type == "rook":
                    all_legal_moves += self.rook_legal_moves(piece_coords)[0]
                
                if piece_type == "bishop":
                    all_legal_moves += self.bishop_legal_moves(piece_coords)[0]
                
                if piece_type == "knight":
                    all_legal_moves += self.knight_legal_moves(piece_coords)[0]
                
                if piece_type == "queen":
                    all_legal_moves += self.queen_legal_moves(piece_coords)[0]
                
                if piece_type == "king":
                    all_legal_moves += self.king_legal_moves(piece_coords)[0]
                
                if piece_type == "pawn":
                    all_legal_moves += self.pawn_threat_map(piece_coords)

        for move in all_legal_moves:
            x, y = move
            if color == "white":
                self.white_threat_map[x][y] = 1
            else:
                self.black_threat_map[x][y] = 1
    
    def convert_threat_map(self, color):
        threat_coords = []
        
        if color == "white":
            for i in range(len(self.white_threat_map)):
                for j in range(len(self.white_threat_map[i])):
                    if self.white_threat_map[i][j] == 1:
                        threat_coords.append((i, j))
        else:
            for i in range(len(self.black_threat_map)):
                for j in range(len(self.black_threat_map[i])):
                    if self.black_threat_map[i][j] == 1:
                        threat_coords.append((i, j))
            
        return threat_coords