import random


def guess_number_one():
    # User is prompted to enter two numbers
    num_one = int(input("Enter the number your range starts with: "))
    num_two = int(input("Enter the number your range ends with: "))

    # Select a random number within the range
    num_random = random.randint(num_one, num_two)

    # Points and opportunities begin
    points = 100
    opportunities = 10

