import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return number % 2 == 0


def ask_question(number):
    print(f"Question: {number}")
    return input('Your answer: ')


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        random_number = random.randint(1, 25)
        answer = ask_question(random_number)
        if answer == 'yes' and is_even(random_number) or answer == 'no' and not is_even(random_number):
            correct_answers += 1
            print("Correct!")
        else:
            correct_answers = 0
            correct_answer = 'yes' if is_even(random_number) else 'no'
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
