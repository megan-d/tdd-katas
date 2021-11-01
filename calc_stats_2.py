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

import statistics


def calculate_stats(elements):
    elements.sort()
    return {
        "minimum": elements[0],
        "maximum": elements[len(elements) - 1],
        "number": len(elements),
        "average": statistics.mean(elements),
    }


def test_minimum_value_is_returned():
    elements = [6, 9, 15, -2, 92, 11]
    stats = calculate_stats(elements)
    assert stats["minimum"] == -2


def test_maximum_value_is_returned():
    elements = [6, 9, 15, -2, 92, 11]
    stats = calculate_stats(elements)
    assert stats["maximum"] == 92


def test_correct_number_of_elements_is_returned():
    elements = [6, 9, 15, -2, 92, 11]
    stats = calculate_stats(elements)
    assert stats["number"] == len(elements)


def test_average_value_is_returned():
    elements = [6, 9, 15, -2, 92, 11]
    stats = calculate_stats(elements)
    assert stats["average"] == statistics.mean(elements)


def test_elements_contains_correct_keys():
    elements = [6, 9, 15, -2, 92, 11]
    stats = calculate_stats(elements)
    assert stats.keys() == {"minimum", "maximum", "number", "average"}
