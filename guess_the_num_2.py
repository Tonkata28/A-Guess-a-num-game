import random


def validating_start_end():

    while True:

        beginning_1 = (input("\n Choose the start of the range for your game(integer): "))
        ending_1 = (input("\n Choose the end of the range for your game(integer): "))

        if beginning_1.strip("-").isdigit() and ending_1.strip("-").isdigit():

            beginning_1, ending_1 = int(beginning_1), int(ending_1)

        else:
            print("\n Start and end of range must be integers! ")
            continue

        if beginning_1 < ending_1:

            return beginning_1, ending_1

        else:
            print("\n Invalid input. Start of range can't be bigger than or equal to the end.")


def yes_answer(answer: str) -> bool:
    return "yes" == answer.lower().strip()


def no_answer(answer: str) -> bool:
    return "no" == answer.lower().strip()


def end_guess(guess: str) -> bool:
    return "end" == guess.lower().strip()


def navigation_user(guess: int, special_num: int, tries: int, counter: int) -> None:

    if guess < special_num:
        print(f"\n The number is bigger than your guess. {tries - counter} tries remaining.")

    elif guess > special_num:
        print(f"\n The number is smaller than your guess. {tries - counter} tries remaining.")


def validating_guess(guess: str, ending_1: int, starting: int) -> \
        bool or None:

    end_flag = end_guess(guess)

    if end_flag:
        print("\n End of the game! Forced manually!")
        return None

    elif not guess.strip("-").isdigit():
        print("\n Invalid input. Your guess must be an integer!")
        return False

    elif int(guess) < starting or int(guess) > ending_1:
        print("\n Invalid input. Guess must be within the chosen range! ")
        return False

    else:
        return True


def range_change_function(beginning: int, ending: int) -> bool or tuple[int, int]:

    range_change = input("\n Would you like to change the range?"
                         "\n Answer with 'yes' or 'no' :")

    if no_answer(answer=range_change):

        print(f"\n Ok, continuing with the range({beginning} - {ending}). ")

        return beginning, ending

    elif yes_answer(answer=range_change):

        beginning, ending = validating_start_end()  # For better readability
        return beginning, ending

    else:
        print("\n Invalid input for changing the range. End of game! ")
        return False


def play_again() -> bool:

    play_again_answer = input(f"\n Would you like to play again?\n Answer with 'yes' or 'no': ")

    if no_answer(answer=play_again_answer):

        print("\n End of the game. See you soon!")
        return False

    elif not yes_answer(answer=play_again_answer):

        print("\n Invalid input! Ending game. ")
        return False

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

        play_again_return = play_again()

        if not play_again_return:
            return

        range_change_return = range_change_function(beginning=beginning, ending=ending)

        if not range_change_return:
            return

        beginning, ending = range_change_return


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
                  
                  " 'Easy - 1 (15 total tries)'\n"
                  " 'Normal - 2 (10 total tries)'\n"
                  " 'Hard - 3 (5 total tries)'\n"
                  " 'Sniper - 4 (1 try)'\n"
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

