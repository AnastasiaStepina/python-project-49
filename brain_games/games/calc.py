import random
import operator
from brain_games.games.even import welcome_user
from brain_games.games.const import PLUS_NUM, MINUS_NUM, MIN_NUMBER, MAX_NUMBER, WRONG_ANSWER, CALC


def random_sign():
    random_math = random.randint(PLUS_NUM, MINUS_NUM)
    if random_math == PLUS_NUM:
        return operator.add, '+'
    elif random_math == MINUS_NUM:
        return operator.sub, '-'
    else:
        return operator.mul, '*'


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation, sign = random_sign()
    print(f"Question: {num1} {sign} {num2}")
    return num1, num2, operation


def main():
    name = welcome_user()
    print(CALC)
    correct_answers = 0
    while correct_answers < 3:
        num1, num2, operation = get_question()
        answer = input('Your answer: ')
        correct_answer = operation(num1, num2)
        if int(answer) == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            correct_answers = 0
            print(f"{answer} {WRONG_ANSWER} {correct_answer}.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
