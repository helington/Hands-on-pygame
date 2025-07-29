from os import path
from pathlib import Path

# Dimensions of the screen
HEIGHT_SCREEN = 400
WIDTH_SCREEN = 800

# Ceil frame rate
FPS = 60

# Paths
ROOT_DIR = Path(__file__).resolve().parents[1]
GRAPHICS_DIR = path.join(ROOT_DIR, 'graphics')
GRAPHICS_SNAIL_DIR = path.join(GRAPHICS_DIR, 'snail')
GRAPHICS_FLY_DIR = path.join(GRAPHICS_DIR, 'Fly')
GRAPHICS_PLAYER_DIR = path.join(GRAPHICS_DIR, 'player')
AUDIO_DIR = path.join(ROOT_DIR, 'audio')
FONT_DIR = path.join(ROOT_DIR, 'font')

# Font settings
FONT_SIZE = 50

# Colors
DARKISH_GRAY = (64, 64, 64)
DARKISH_CYAN = (94, 129, 162)
LIGHT_CYAN = (111, 196, 169)

# Positions
FLOOR_Y = 300
EXCEEDED_OBSTSCLE_X = -100

# Button videogame
START_VIDEO_GAME_BUTTON = 6
