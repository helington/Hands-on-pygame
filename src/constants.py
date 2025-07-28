from pathlib import Path
from os import path

# Dimensions of the screen
HEIGHT_SCREEN = 400
WIDTH_SCREEN = 800

# Ceil frame rate 
FPS = 60

# Paths
ROOT_DIR = Path(__file__).resolve().parents[1]
GRAPHICS_DIR = path.join(ROOT_DIR, 'graphics')
GRAPHICS_SNAIL_DIR = path.join(GRAPHICS_DIR, 'snail')
GRAPHICS_PLAYER_DIR = path.join(GRAPHICS_DIR, 'player')
AUDIO_DIR = path.join(ROOT_DIR, 'audio')
FONT_DIR = path.join(ROOT_DIR, 'font')

# Font settings
FONT_SIZE = 50