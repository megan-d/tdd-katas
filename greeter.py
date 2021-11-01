# Before you start:
# Try not to read ahead.
# Do one task at a time. The trick is to learn to work incrementally.
# This kata demonstrates the problems of static scoped functions and objects.

# All tests should always pass, regardless of environment conditions.

# Write a Greeter class with greet function that receives a name as input and outputs Hello <name>. The signature of greet should not change throughout the kata. You are allowed to construct Greeter object as you please.
# greet trims the input
# greet capitalizes the first letter of the name
# greet returns Good morning <name> when the time is 06:00-12:00
# greet returns Good evening <name> when the time is 18:00-22:00
# greet returns Good night <name> when the time is 22:00-06:00
# greet logs into console each time it is called


class Greet:
    def __init__(self, name):
        self.name = name


def test_greet_outputs_hello_with_input():
    name = input("Enter name: ")
    greeting = Greet(name)
    assert greeting.message == "Hello " + name
