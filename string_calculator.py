import pytest

# Create a simple calculator that takes a String and returns a integer
#
# Signature (pseudo code):
#
# int Add(string numbers)
# Requirements
# 1. The method can take up to two numbers, separated by commas, and will return their sum as a result. So the inputs can be: “”, “1”, “1,2”. For an empty string, it will return 0.
#
# Notes:
#
# start with the simplest case (empty string) and extend it with the more advanced cases (“1” and “1,2”) step by step
# keep the three rules in mind and always write just sufficient enough code
# do not forget to refactor your code after each passing test
# 2. Allow the add method to handle an unknown number of arguments
#
# 3. Allow the add method to handle newlines as separators, instead of comas
#
# “1,2\n3” should return “6”
# “2,\n3” is invalid, but no need to clarify it with the program


def add(x):
    sum = 0
    if x == "":
        return sum
    list_of_values = x.split(",")
    for val in list_of_values:
        sum += int(val)
    return sum


def test_empty_string_returns_0():
    assert add("") == 0


def test_single_value_returns_itself():
    assert add("4") == 4


def test_two_values_returns_sum():
    assert add("1,2") == 3


def test_can_handle_unknown_num_of_args():
    assert add("1,2,3,4") == 10


if __name__ == "__main__":
    add()