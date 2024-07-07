import random


def get_min_max():
    while True:
        try:
            min_num = int(input("Minimal number: "))
            max_num = int(input("Maximum number: "))
            if min_num > max_num:
                print("Min value musn't be greater than max value!")
            else:
                print(f"Secret number is between \033[1m{min_num}\033[0m and \033[1m{max_num}\033[0m")
                return min_num, max_num
        except ValueError:
            print("Not a valid number! Please enter integers.")


def guess_number(min_num, max_num):
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < min_num or guess > max_num:
                print(f"Maybe try again with a number between \033[1m{min_num}\033[0m and \033[1m{max_num}\033[0m ;)")
            elif guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print(f"Correct! The secret number is \033[1m{secret_number}\033[0m")
                print(f"You got it in \033[1m{attempts}\033[0m attempts.")
                break
        except ValueError:
            print("Not a valid number!")


def main_game():
    while True:
        min_num, max_num = get_min_max()
        guess_number(min_num, max_num)
        play_again = input("Another game? Write anything to play again, or just press Enter to end game: ")
        if play_again == "":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main_game()
