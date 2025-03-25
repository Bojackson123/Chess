import pygame
from game.button import Button
from game.board import Board
from game.pieces import Pieces
from game import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE_FONT, FONT, BLACK, WHITE, FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def mainMenu():
    title = TITLE_FONT.render("Chess", True, WHITE)
    play_button = Button(SCREEN_WIDTH // 2 - 75, 350, 150, 50, "PLAY", WHITE, WHITE, FONT, BLACK)
    quit_button = Button(SCREEN_WIDTH // 2 - 75, 440, 150, 50, "QUIT", WHITE, WHITE, FONT, BLACK)
    
    
    while True:
        screen.fill(BLACK)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 160))
        
        mouse_pos = pygame.mouse.get_pos()
        
         # Check hover state for both buttons
        is_play_hovering = play_button.update(mouse_pos)
        play_button.draw(screen)
        
        is_quit_hovering = quit_button.update(mouse_pos)
        quit_button.draw(screen)
        
        # Change cursor based on hover state
        if is_play_hovering or is_quit_hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Pointer cursor
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Default cursor
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                
            is_play_clicked = play_button.is_clicked(event)
            is_quit_clicked = quit_button.is_clicked(event)
            
            if is_play_clicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                play()
            elif is_quit_clicked:
                pygame.QUIT()
                return
        
        pygame.display.flip()
        
        clock.tick(FPS) 
        

def play():
    game_board = Board()
    # print(game_board.tiles)
    pieces = Pieces("black")
    print(pieces.board)
    # print(pieces.white_threat_map)
    # print(pieces.black_threat_map)
    
    
    while True:
        game_board.draw(screen)
        pieces.draw_pieces(screen)
        legal_moves = pieces.legal_moves(pieces.selected_piece)
        capture_moves = pieces.capture_moves(pieces.selected_piece)
        filtered_legal_moves = [move for move in legal_moves if move not in capture_moves]
        game_board.legal_draw(filtered_legal_moves, screen)
        game_board.capture_draw(capture_moves, screen)
        
        pieces.generate_threat_map("white")
        test_list = pieces.convert_threat_map("white")
        game_board.test_draw(test_list, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    # Handle clicking when a piece is selected
                    if pieces.is_piece_selected():
                        selected_piece_coords = pieces.get_piece_coords(mouse_pos)

                        # Capture logic: Clicked on an opponent's piece
                        if pieces.has_piece(mouse_pos) and pieces.board[selected_piece_coords][1] != pieces.turn:
                            if pieces.is_legal_move(mouse_pos):
                                pieces.move_piece(mouse_pos)
                                game_board.remove_all_highlights()
                                pieces.deselect_piece()

                        # Switching piece logic: Clicked on another valid piece of the same color
                        elif pieces.has_piece(mouse_pos) and pieces.board[selected_piece_coords][1] == pieces.turn:
                            pieces.deselect_piece()
                            game_board.highlight_yellow(mouse_pos)
                            pieces.select_piece(mouse_pos)
                            print(f"Switched to new piece: {pieces.selected_piece}")

                        # Regular move logic: Clicked an empty square or valid move tile
                        elif pieces.is_legal_move(mouse_pos):
                            pieces.move_piece(mouse_pos)
                            game_board.remove_all_highlights()
                            pieces.deselect_piece()

                        # If it's an invalid click, just deselect
                        else:
                            game_board.remove_all_highlights()
                            pieces.deselect_piece()

                    # No piece selected yet: Handle selecting a new piece
                    elif pieces.has_piece(mouse_pos):
                        selected_piece_coords = pieces.get_piece_coords(mouse_pos)
                        if pieces.board[selected_piece_coords][1] == pieces.turn:
                            game_board.highlight_yellow(mouse_pos)
                            pieces.select_piece(mouse_pos)
                            print(f"New selected piece: {pieces.selected_piece}")
                        else:
                            print("Not your piece!")

                    # Clean up highlights
                    
                    print(pieces.is_piece_selected())







                    
                    
        pygame.display.flip()
        
        clock.tick(FPS)

mainMenu()