import random
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER
RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num2 != 0:
        num2, num1 = num1 % num2, num2
    return num1


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {num1} {num2}"
    correct_answer = str(get_gcd(num1, num2))
    return question, correct_answer


if __name__ == '__main__':
    get_question()
