def convert(km, cel, kg, lit):
    miles = km * 0.621371
    fahrenheit = (cel * 1.8) + 32
    lbs = round(kg / 0.45359237, 7)
    gals = round(lit / 3.785411784, 7)
    return miles, fahrenheit, lbs, gals


def test_convert_returns_correct_values():
    converted_values = convert(1, 30, 5, 3.785411784)
    assert converted_values[0] == 0.621371
    assert converted_values[1] == 86
    assert converted_values[2] == 11.02311310
    assert converted_values[3] == 1


if __name__ == "__main__":
    convert()
