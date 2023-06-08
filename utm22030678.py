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

  # While loop
    while opportunities > 0:
        # Ask the user to enter a number
        user_num = int(
            input(f"Guess the number between {num_one} and {num_two}: "))

        # Compare user number with random number
        if user_num == num_random:
            print("You guessed it, congratulations!")
            break
        else:
            points -= 10
            opportunities -= 1
            print("Wrong number, try again")
            print(f"Remaining points: {points}")
            print(f"Remaining opportunities: {opportunities}")
