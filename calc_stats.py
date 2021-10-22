# Your task is to process a sequence of integer numbers to determine the following statistics:
# minimum value
# maximum value
# number of elements in the sequence
# average value
# For example: [6, 9, 15, -2, 92, 11]
# minimum value = -2
# maximum value = 92
# number of elements in the sequence = 6
# average value = 21.833333

import pytest
import statistics


VALUES = [6, 9, 15, -2, 92, 11]


def generate_stats(values):
    values.sort()
    stats = {
        "minimum": values[0],
        "maximum": values[len(values) - 1],
        "number": len(values),
        "average": statistics.mean(values),
    }
    return stats


def test_returns_expected_keys():
    stats = generate_stats(VALUES)
    expected_keys = {"minimum", "maximum", "number", "average"}
    assert stats.keys() == expected_keys


def test_returns_correct_minimum_value():
    test_values = [6, 9, 15, -2, 92, 11]
    result = generate_stats(test_values)
    assert result["minimum"] == -2


def test_returns_correct_maximum_value():
    test_values = [6, 9, 15, -2, 92, 11]
    result = generate_stats(test_values)
    assert result["maximum"] == 92


def test_returns_correct_number_of_elements():
    test_values = [6, 9, 15, -2, 92, 11]
    result = generate_stats(test_values)
    assert result["number"] == 6


def test_returns_correct_average_value():
    test_values = [6, 9, 15, -2, 92, 11]
    result = generate_stats(test_values)
    assert result["average"] == statistics.mean(test_values)
