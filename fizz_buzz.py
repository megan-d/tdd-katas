import pytest

# Rules:
# 1. Print numbers 1-100
# 2. For multiples of 3 print "Fizz"
# 3. For multiples of 5 print "Buzz"
# 4. For multiples of both 3 and 5 print "FizzBuzz"


def fizz_buzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "FizzBuzz"
    elif x % 5 == 0:
        return "Buzz"
    elif x % 3 == 0:
        return "Fizz"
    else:
        return x


def main():
    for i in range(1, 101):
        print(fizz_buzz(i))


def test_multiples_of_3_return_Fizz():
    assert fizz_buzz(3) == "Fizz"


def test_multiples_of_5_return_Buzz():
    assert fizz_buzz(5) == "Buzz"


def test_multiples_of_3_and_5_return_FizzBuzz():
    assert fizz_buzz(15) == "FizzBuzz"


if __name__ == '__main__':
    main()
