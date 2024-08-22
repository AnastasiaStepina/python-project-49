import random
import prompt
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER, WRONG_ANSWER, EVEN, WELCOME


def welcome_user():
    name = prompt.string(WELCOME)
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return number % 2 == 0


def get_question(number):
    print(f"Question: {number}")
    return input('Your answer: ')


def main():
    name = welcome_user()
    print(EVEN)
    correct_answers = 0
    while correct_answers < 3:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        answer = get_question(random_number)
        if answer == 'yes' and is_even(random_number) or answer == 'no' and not is_even(random_number):
            correct_answers += 1
            print("Correct!")
        else:
            correct_answers = 0
            correct_answer = 'yes' if is_even(random_number) else 'no'
            print(f"{answer} {WRONG_ANSWER} {correct_answer}.")
            print(f"Let's try again, {name}!")

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
