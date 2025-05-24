import random
print("Type in 'End' instead of a guess if you would like the program to finish manually.")
start = int(input("Choose the start of the range for your game(integer): "))
end = int(input("Choose the end of the range for your game(integer): "))
modes_available = 4
is_beginning = True
amount_played = 0


def guessing_the_num(tries: int) -> None:
    special_num = random.randint(start, end)
    guess = (input(f"Type in your guess for the number({start} - {end}): "))
    counter = 0

    while True:
        if not guess.isdigit() and guess != "End":
            print("Invalid input. Try again.")
            guess = (input(f"Type in your guess for the number({start} - {end}): "))
            continue

        counter += 1

        if guess == "End":
            print("End of the game!")
            break
        elif counter == tries and int(guess) != special_num:
            continuing_question = input(f"Your attempts have finished! The number was {special_num}.\n"
                                        "Would you like to try again?\n"
                                        "Enter your answer here('yes' or 'no'): ")
            if 'yes' in continuing_question.lower():
                attempts_2 = second_part()

                if attempts is None:
                    print("End of program")
                    break

                guessing_the_num(tries=attempts_2)

            elif 'no' in continuing_question.lower():
                print("Thanks for playing. See you soon!")

            else:
                print("Invalid input!")
            break

        guess = int(guess)

        if guess == special_num:
            print(f"Congratulations, you guessed the special number - {special_num}")
            break

        if guess > end or guess < start:
            print("Invalid input. Try again.")
            guess = (input(f"Type in your guess for the number({start} - {end}): "))
            continue

        elif guess < special_num:
            print("The number is bigger than your guess.")

        elif guess > special_num:
            print("The number is smaller than your guess.")

        guess = (input(f"Type in your guess for the number({start} - {end}): "))


def second_part() -> int or None:
    mode = int(input("Which mode would you like to play?\n"
                     f"There are currently {modes_available} modes.\n"
                     "'Easy - 1'\n"
                     "'Normal - 2'\n"
                     "'Hard - 3'\n"
                     "'Sniper - 4'\n"
                     "Enter your corresponding number here: "))

    if mode == 1:
        return 15
    elif mode == 2:
        return 10
    elif mode == 3:
        return 5
    elif mode == 4:
        return 1
    else:
        return None


attempts = second_part()

if attempts is None:
    print("Invalid input for choosing mode. End of program!")
else:
    guessing_the_num(tries=attempts)