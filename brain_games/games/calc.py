import random
import operator
from brain_games.games.const import PLUS_NUM, MINUS_NUM, MIN_NUMBER, MAX_NUMBER
RULES = 'What is the result of the expression?'


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
    question = f"Question: {num1} {sign} {num2}"
    correct_answer = str(operation(num1, num2))
    return question, correct_answer


if __name__ == '__main__':
    get_question()
