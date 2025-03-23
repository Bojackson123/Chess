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
    test_moves = pieces.king_possible_moves((3,0))
    print(test_moves)
    
    while True:
        game_board.draw(screen)
        pieces.draw_pieces(screen)
        #game_board.test_draw(test_moves,screen)
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1 and pieces.has_piece(mouse_pos):
                    game_board.highlight_yellow(mouse_pos)
                    pieces.select_piece(mouse_pos)
                    print(pieces.selected_piece)
                    
                elif event.button == 1 and pieces.is_piece_selected() and pieces.is_turns_piece():
                    pieces.move_piece(mouse_pos)
                    game_board.remove_all_highlights()      
                else:
                    game_board.remove_all_highlights()
                    #pieces.deselect_piece()
                print(pieces.is_piece_selected())
                if event.button == 3:
                    game_board.add_remove_highlight("right", mouse_pos)
                    
                    
        pygame.display.flip()
        
        clock.tick(FPS)

mainMenu()