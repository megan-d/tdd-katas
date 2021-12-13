import pytest
from bowling3 import Game


def test_gutter_ball_game():
    game = Game()
    for roll in range(20):
        game.roll(0)
    assert game.score() == 0


def test_all_twos_game():
    game = Game()
    for roll in range(20):
        game.roll(2)
    assert game.score() == 40


def test_strike_game():
    game = Game()
    game.roll(10)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 30


def test_spare_game():
    game = Game()
    game.roll(8)
    game.roll(2)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 29
