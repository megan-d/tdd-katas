import pytest
from bowling import Game


def test_gutter_game():
    game = Game()
    for roll in range(20):
        game.roll(0)
    assert game.score() == 0


def test_all_ones_game():
    game = Game()
    for roll in range(20):
        game.roll(1)
    assert game.score() == 20


def test_strike():
    game = Game()
    game.roll(10)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 30


def test_spare():
    game = Game()
    game.roll(2)
    game.roll(8)
    for roll in range(18):
        game.roll(1)
    assert game.score() == 29
