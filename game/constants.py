import pygame 
import os, io

pygame.init()

# Game Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

FONT_TITLE_SIZE = 200
FONT_SIZE = 40
FONT_PATH = os.path.join(os.path.dirname(__file__), "../assets/fonts/8bit.ttf")
TITLE_FONT = pygame.font.Font(FONT_PATH, FONT_TITLE_SIZE)
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)

# Colors 
WHITE = (235,236,208)
BLACK = (0, 0, 0)
GREEN = (115,149,82)
YELLOW = (245,246,130)
RED = (235,125,106)

# Pieces
WHITE_PIECES = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

WHITE_LOCATIONS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),

                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]


BLACK_PIECES = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

BLACK_LOCATIONS = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),

                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt", encoding="utf-8").read()
    start = svg_string.find('<svg')    
    if start > 0:
        svg_string = svg_string[:start+4] + f' transform="scale({scale})"' + svg_string[start+4:]
    return pygame.image.load(io.BytesIO(svg_string.encode()))
scale = 2.15

# White Images
white_rook = load_and_scale_svg('./assets/pieces/white/white-rook.svg', scale)
white_knight = load_and_scale_svg('./assets/pieces/white/white-knight.svg', scale)
white_bishop = load_and_scale_svg('./assets/pieces/white/white-bishop.svg', scale)
white_king = load_and_scale_svg('./assets/pieces/white/white-king.svg', scale)
white_queen = load_and_scale_svg('./assets/pieces/white/white-queen.svg', scale)
white_pawn = load_and_scale_svg('./assets/pieces/white/white-pawn.svg', scale)


WHITE_IMAGES = {
    "rook" : white_rook,
    "knight" : white_knight,
    "bishop" : white_bishop,
    "king" : white_king,
    "queen" : white_queen,
    "pawn" : white_pawn
    }


# Black Images 
black_rook = load_and_scale_svg('./assets/pieces/black/black-rook.svg', scale)
black_knight = load_and_scale_svg('./assets/pieces/black/black-knight.svg', scale)
black_bishop = load_and_scale_svg('./assets/pieces/black/black-bishop.svg', scale)
black_king = load_and_scale_svg('./assets/pieces/black/black-king.svg', scale)
black_queen = load_and_scale_svg('./assets/pieces/black/black-queen.svg', scale)
black_pawn = load_and_scale_svg('./assets/pieces/black/black-pawn.svg', scale)


BLACK_IMAGES = {
    "rook" : black_rook,
    "knight" : black_knight,
    "bishop" : black_bishop,
    "king" : black_king,
    "queen" : black_queen,
    "pawn" : black_pawn
}