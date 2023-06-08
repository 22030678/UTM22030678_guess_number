while opportunities > 0:
        print("\nHave", opportunities, "opportunities y",
              points_player2, "points.")

        number_two = int(input("player 2, enter a number: "))

        if number_two == secret_number:
            print("¡Congratulations, Player 2! You have guessed the number correctly.")
            break
        else:
            print("Wrong number. you lose 10 points.")
            points_player2 -= 10
            opportunities -= 1

    print("\nThe game is over.")
    if points_player2 > 0:
        print("Final points of Player 2:", points_player2)
    else:
        print("Player 2 has no points. Better luck next time.")


guess_number_two()
