from pathlib import Path
from os import path

HEIGHT_SCREEN = 400
WIDTH_SCREEN = 800

FPS = 60

ROOT_DIR = Path(__file__).resolve().parents[1]

GRAPHICS_DIR = path.join(ROOT_DIR, 'graphics')
AUDIO_DIR = path.join(ROOT_DIR, 'audio')
FONT_DIR = path.join(ROOT_DIR, 'font')
