from game import Bolas, Ball
from pygame import Surface
import pygame

def test_create_screen():
    bolas = Bolas()
    assert isinstance(bolas.screen, Surface)
    assert bolas.screen.get_width() == 800
    assert bolas.screen.get_height() == 600 

    assert pygame.display.get_caption()[0] == "Bolas"

def test_exist_one_ball():
    bolas = Bolas()

    assert isinstance(bolas.player, Ball)
    assert bolas.player.x == 400
    assert bolas.player.y == 300
    assert bolas.player.radio == 30
    