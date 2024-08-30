import random
from brain_games.games.const import MIN_NUMBER, MAX_PROGR
RULES = 'What number is missing in the progression?'


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_PROGR)
    num2 = random.randint(MIN_NUMBER, MAX_PROGR)
    length = 10
    numbers = [num1 + i * num2 for i in range(length)]
    index = random.randint(0, 9)
    correct_answer = str(numbers[index])
    numbers[index] = ".."
    question = f"Question: {' '.join(map(str, numbers))}"
    return question, correct_answer


if __name__ == '__main__':
    get_question()
