# Prior to 1582, the Julian Calendar was in wide use and defined leap years as every year divisible by 4. However, it was found in the late 16th century that the calendar year had drifted from the solar year by approximately 10 days. The Gregorian Calendar was defined in order to thin out the number of leap years and to more closely align the calendar year with the solar year. It was adopted in Papal countries on October 15, 1582, skipping 10 days from the Julian Calendar date. Protestant countries adopted the Gregorian Calendar after some time.

# User Story:
# As a user, I want to know if a year is a leap year, So that I can plan for an extra day on February 29th during those years.
# Acceptance Criteria:
# All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year),
# All years divisible by 100 but not by 400 are NOT leap years (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year),
# All years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016),
# All years not divisible by 4 are NOT leap years (e.g. 2017, 2018, 2019).


def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def test_divisible_by_400_returns_true():
    assert is_leap(800) is True
    assert is_leap(1200) is True
    assert is_leap(2000) is True


def test_divisible_by_100_but_not_400_returns_false():
    assert is_leap(1700) is False
    assert is_leap(1800) is False
    assert is_leap(1900) is False
    assert is_leap(2100) is False


def test_divisible_by_4_but_not_100_returns_true():
    assert is_leap(2008) is True
    assert is_leap(2012) is True
    assert is_leap(2016) is True


def test_not_divisible_by_4_returns_false():
    assert is_leap(2017) is False
    assert is_leap(2018) is False
    assert is_leap(2019) is False


if __name__ == "__main__":
    is_leap()
