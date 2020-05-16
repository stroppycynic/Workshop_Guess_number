import random


def get_user_number():
    while True:
        try:
            user_number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return user_number


def number_guesser():
    computer_number = random.randint(1, 100)
    input_number = get_user_number()
    while input_number != computer_number:
        if input_number < computer_number:
            print("Too small!")
        else:
            print("Too big")
        input_number = get_user_number()
    print("You win!")


if __name__ == '__main__':
    number_guesser()