import pytest
from bowling2 import Game


def test_all_gutter_balls():
    game = Game()
    for roll in range(20):
        game.roll(0)
    assert game.score() == 0


def test_all_ones_game():
    game = Game()
    for roll in range(20):
        game.roll(1)
    assert game.score() == 20


def test_spare():
    game = Game()
    game.roll(8)
    game.roll(2)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 29


def test_strike():
    game = Game()
    game.roll(10)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 30
