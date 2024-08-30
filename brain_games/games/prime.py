import random
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def get_question():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {num}"
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


if __name__ == '__main__':
    get_question()
