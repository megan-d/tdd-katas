import pytest

# Rules:
# 1. Print numbers 1-100
# 2. For multiples of 3 print "Fizz"
# 3. For multiples of 5 print "Buzz"
# 4. For multiples of both 3 and 5 print "FizzBuzz"


def fizz_buzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return x


def main():
    for i in range(1, 101):
        print(fizz_buzz(i))


def test_value_is_returned():
    value = fizz_buzz(3)
    assert value


def test_multiples_of_3_return_Fizz():
    assert fizz_buzz(9) == "Fizz"


def test_multiples_of_5_return_Buzz():
    assert fizz_buzz(10) == "Buzz"


def test_multiples_of_both_return_FizzBuzz():
    assert fizz_buzz(15) == "FizzBuzz"


if __name__ == "__main__":
    main()