import random


def validating_start_end():

    while True:

        beginning_1 = (input("\n Choose the start of the range for your game(integer): "))
        ending_1 = (input("\n Choose the end of the range for your game(integer): "))

        if not beginning_1.isdecimal() or not ending_1.isdecimal():

            print("\n Starting and ending must be integers!")
            continue

        beginning_1, ending_1 = int(beginning_1), int(ending_1)

        if beginning_1 < ending_1:
            return beginning_1, ending_1
        else:
            print("\n Invalid input. Start of range can't be bigger than or equal to the end.")


def yes_answer(question: str) -> bool:
    return "yes" == question.lower().strip()


def no_answer(question: str) -> bool:
    return "no" == question.lower().strip()


def end_guess(guess: str) -> bool:
    return "end" == guess.lower().strip()


def navigation_user(guess: int, special_num: int, tries: int, counter: int) -> None:

    if guess < special_num:
        print(f"\n The number is bigger than your guess. {tries - counter} tries remaining.")

    elif guess > special_num:
        print(f"\n The number is smaller than your guess. {tries - counter} tries remaining.")


def validating_guess(guess: str, ending_1: int, starting: int) -> bool or None:

    end_flag = end_guess(guess)

    if end_flag:
        print("\n End of the game! Forced manually!")
        return None

    elif not guess.isdigit():
        print("\n Invalid input. Your guess must be an integer!")
        return False

    elif int(guess) < starting or int(guess) > ending_1:
        print("\n Invalid input. Guess must be within the chosen range! ")
        return False

    else:
        return True


def play_game():

    beginning, ending = validating_start_end()

    while True:

        attempts = choosing_difficulty()

        if attempts is None:
            print("\n Invalid input for choosing mode. End of program!")
            return

        if not guessing_the_num(start=beginning, end= ending, tries=attempts):
            return

        play_again = input(f"\n Would you like to play again?\n Answer with 'yes' or 'no': ")

        if no_answer(question=play_again):

            print("\n End of the game. See you soon!")
            return

        elif not yes_answer(question=play_again):

            print("\n Invalid input! Ending game. ")
            return

        range_change = input("\n Would you like to change the range?"
                             "\n Answer with 'yes' or 'no' :")

        if no_answer(question=range_change):

            print(f"\n Ok, continuing with the range({beginning} - {ending}). ")
            continue

        elif yes_answer(question=range_change):

            beginning, ending = validating_start_end()

        else:
            print("\n Invalid input for changing the range. End of game! ")
            return


def guessing_the_num(start: int, end: int, tries: int) -> bool:

    special_num = random.randint(start, end)
    counter = 0

    while True:
        guess_input = input(f"\n Type in your guess for the number({start} - {end}): ")

        is_valid = validating_guess(guess=guess_input, starting=start, ending_1=end)

        if is_valid is None:
            return False

        elif not is_valid:
            continue

        guess = int(guess_input)
        counter += 1

        if guess == special_num:

            print(f"\n Congratulations, you guessed the special number - {special_num}.")
            return True

        elif counter == tries:

            print(f"\n Your attempts have finished! The number was {special_num}.\n")
            return True

        navigation_user(guess=guess, special_num=special_num, tries=tries, counter=counter)


def choosing_difficulty() -> int or None:
    mode = (input("\n Which mode would you like to play?\n"
            f" There are currently {modes_available} modes.\n"
                  " 'Easy - 1'\n"
                  " 'Normal - 2'\n"
                  " 'Hard - 3'\n"
                  " 'Sniper - 4'\n"
                  " Enter your corresponding number here: "))

    if not mode.isdecimal():
        return None

    mode_number = int(mode)
    if mode_number == 1:
        return 15
    elif mode_number == 2:
        return 10
    elif mode_number == 3:
        return 5
    elif mode_number == 4:
        return 1
    else:
        return None


if __name__ == "__main__":
    modes_available = 4

    print("\n Type in 'End' instead of a guess if you would like the program to finish manually.")

    print("\n All guesses must be positive integers. Enjoy! ")

    play_game()

