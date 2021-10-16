# Implement a city search functionality. The function takes a string (search text) as input and returns the found cities which corresponds to the search text.

# Requirements
# 1. If the search text is fewer than 2 characters, then should return no results. (It is an optimization feature of the search functionality.)

# 2. If the search text is equal to or more than 2 characters, then it should return all the city names starting with the exact search text.
# For example for search text “Va”, the function should return Valencia and Vancouver

# 3. The search functionality should be case insensitive

# 4. The search functionality should work also when the search text is just a part of a city name
# For example “ape” should return “Budapest” city

# 5. If the search text is a “*” (asterisk), then it should return all the city names.

cities = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def search(search_text=""):
    search_cities = [city.lower() for city in cities]
    if search_text == "*":
        return cities
    if len(search_text) < 2:
        return None
    matches = list(filter(lambda cities: search_text.lower() in cities, search_cities))
    formatted_matches = [match.title() for match in matches]
    return formatted_matches


def test_returns_all_city_names():
    search_results = search(search_text="*")
    assert search_results == cities


def test_returns_no_results_if_search_fewer_than_two_characters():
    search_results = search(search_text="a")
    assert search_results == None


def test_results_are_case_insensitive():
    search_results = search(search_text="rOmE")
    assert search_results == ["Rome"]


def test_results_are_case_insensitive_multiple_words():
    search_results = search(search_text="hONg kOnG")
    assert search_results == ["Hong Kong"]


def test_results_are_shown_if_multiple_letters_match_beginning():
    search_results = search(search_text="Va")
    assert search_results == ["Valencia", "Vancouver"]


def test_results_are_shown_if_multiple_letters_match_middle():
    search_results = search(search_text="on")
    search_results_two = search(search_text="ape")
    assert search_results == ["London", "Hong Kong"]
    assert search_results_two == ["Budapest"]