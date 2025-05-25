import random

print("\n Type in 'End' instead of a guess if you would like the program to finish manually.")

while True:

    beginning = int(input("\n Choose the start of the range for your game(integer): "))
    ending = int(input("\n Choose the end of the range for your game(integer): "))

    if beginning < ending:
        break

    print("\n Invalid input. Start of range can't be bigger than the end.")
modes_available = 4


def yes_in_question(question: str) -> bool:
    return "yes" in question.lower().strip()


def no_in_question(question: str) -> bool:
    return "no" in question.lower().strip()


def end_in_guess(guess: str) -> bool:
    return "end" in guess.lower().strip()


def guessing_the_num(start: int, end: int, tries: int) -> None:
    special_num = random.randint(start, end)
    counter = 0

    while True:
        guess = (input(f"\n Type in your guess for the number({start} - {end}): "))

        if not guess.isdigit() and not end_in_guess(guess):
            print("\n Invalid input. Try again.")
            continue

        if end_in_guess(guess):
            print("\n End of the game!")
            break
            
        counter += 1
        guess = int(guess)

        if (counter == tries and guess != special_num) or guess == special_num:
            start_1 = 0
            end_1 = 0
            continuing_question = ""
            second_question = ""
            range_changed = True

            if counter == tries and guess != special_num:
                continuing_question = input(f"\n Your attempts have finished! The number was {special_num}.\n"
                                            " Would you like to try again?\n"
                                            " Enter your answer here('yes' or 'no'): ")

            if guess == special_num:
                print(f"\n Congratulations, you guessed the special number - {special_num}")
                continuing_question = input(" Would you like to play again?\n"
                                            " Answer with 'yes' or 'no': ")

            if no_in_question(continuing_question):
                print("\n End of the game. See you soon!")
                break

            elif yes_in_question(continuing_question):

                second_question = input("\n Would you like to change the range?\n"
                                        " Answer with 'yes' or 'no': ")

                if yes_in_question(second_question):
                    start_1 = int(input("\n Choose the start of the range for your game(integer): "))
                    end_1 = int(input("\n Choose the end of the range for your game(integer): "))

                elif no_in_question(second_question):
                    print(f"\n Ok, continuing with the range({start} - {end})")
                    range_changed = False

                else:
                    print("\n Invalid input. End of the game.")
                    break

                attempts_2 = second_part()

                if attempts_2 is None:
                    print("\n End of program")
                    break

                if range_changed:
                    guessing_the_num(start=start_1, end=end_1, tries=attempts_2)
                else:
                    guessing_the_num(start=beginning, end=ending, tries=attempts_2)

            else:
                print("\n Invalid input!")

            break

        if guess > end or guess < start:
            print("\n Invalid input. Try again.")
            continue

        elif guess < special_num:
            print(f"\n The number is bigger than your guess. {tries - counter} tries remaining.")

        elif guess > special_num:
            print(f"\n The number is smaller than your guess. {tries - counter} tries remaining.")


def second_part() -> int or None:
    mode = int(input("\n Which mode would you like to play?\n"
                     f" There are currently {modes_available} modes.\n"
                     " 'Easy - 1'\n"
                     " 'Normal - 2'\n"
                     " 'Hard - 3'\n"
                     " 'Sniper - 4'\n"
                     " Enter your corresponding number here: "))

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
    print("\n Invalid input for choosing mode. End of program!")
else:
    guessing_the_num(start=beginning, end=ending, tries=attempts)
