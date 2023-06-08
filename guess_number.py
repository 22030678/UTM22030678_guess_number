def guess_number_two():

    number_one = int(input("Enter the start number of the range: "))
    number_two = int(input("Enter the ending number of the range: "))

    secret_number = int(input("Player 1, choose a number within the range: "))
    if secret_number < number_one or secret_number > number_two:
        print("The selected number is out of range. Try again.")
        return

    points_player2 = 100
    opportunities = 10
