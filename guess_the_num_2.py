import random

print("Type in 'End' instead of a guess if you would like the program to finish manually.")
beginning = int(input("Choose the start of the range for your game(integer): "))
ending = int(input("Choose the end of the range for your game(integer): "))
modes_available = 4


def guessing_the_num(start: int, end: int, tries: int) -> None:
    special_num = random.randint(start, end)
    guess = (input(f"Type in your guess for the number({start} - {end}): "))
    counter = 0

    while True:
        if not guess.isdigit() and guess != "End":
            print("Invalid input. Try again.")
            guess = (input(f"Type in your guess for the number({start} - {end}): "))
            continue

        if guess == "End":
            print("End of the game!")
            break
            
        counter += 1
        guess = int(guess)
        if (counter == tries and guess != special_num) or guess == special_num:

            if counter == tries and guess != special_num:
                continuing_question = input(f"Your attempts have finished! The number was {special_num}.\n"
                                            "Would you like to try again?\n"
                                            "Enter your answer here('yes' or 'no'): ")

                if "no" in continuing_question.lower():
                    print("End of the game. See you soon!")
                    break

            if guess == special_num:
                print(f"Congratulations, you guessed the special number - {special_num}")
                continuing_question = input("Would you like to play again?\n"
                                            "Answer with 'yes' or 'no': ")

                if "no" in continuing_question.lower():
                    print("End of the game. See you soon!")
                    break

            second_question = input("Would you like to change the range?\n"
                                    "Answer with 'yes' or 'no': ")
            is_different = True
            if 'yes' in second_question.lower():
                start_1 = int(input("Choose the start of the range for your game(integer): "))
                end_1 = int(input("Choose the end of the range for your game(integer): "))
            elif "no" in second_question.lower():
                print(f"Ok, continuing with the range{start} - {end})")
                is_different = False
            else:
                print("Invalid input. End of the game.")
                break

            if 'yes' in continuing_question.lower():
                attempts_2 = second_part()

                if attempts_2 is None:
                    print("End of program")
                    break

                if is_different:
                    guessing_the_num(start=start_1, end=end_1, tries=attempts_2)
                else:
                    guessing_the_num(start=beginning, end=ending, tries=attempts_2)

            else:
                print("Invalid input!")

            break

        if guess > end or guess < start:
            print("Invalid input. Try again.")
            guess = (input(f"Type in your guess for the number({start} - {end}): "))
            continue

        elif guess < special_num:
            print(f"The number is bigger than your guess. {tries - counter} tries remaining.")

        elif guess > special_num:
            print(f"The number is smaller than your guess. {tries - counter} tries remaining.")

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
    guessing_the_num(start=beginning, end=ending, tries=attempts)
