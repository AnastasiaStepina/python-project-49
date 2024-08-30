import random
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question():
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {random_number}"
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer


if __name__ == '__main__':
    get_question()
