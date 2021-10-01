import pytest


def greet(name=["my friend"]):
    names = ""
    is_upper = False
    for nm in name:
        names = names + nm
        if nm.isupper():
            is_upper = True
    if len(name) > 1:
        return f"Hello, {name[0]} and {name[1]}."
    if is_upper:
        return f"HELLO, {names}!"
    else:
        return f"Hello, {names}."


def test_greet_returns_name():
    name = ["Barb"]
    assert greet(name) == "Hello, Barb."


def test_greet_returns_message():
    assert greet(["Bob"]) == "Hello, Bob."


def test_greet_returns_default():
    assert greet() == "Hello, my friend."


def test_greet_returns_shouting_with_capital():
    assert greet(["JERRY"]) == "HELLO, JERRY!"


def test_greet_returns_two_input_names():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."