import random
from brain_games.games.even import welcome_user
from brain_games.games.const import MIN_NUMBER, MAX_PROGR, WRONG_ANSWER, PROGRESSION


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_PROGR)
    num2 = random.randint(MIN_NUMBER, MAX_PROGR)
    length = 10
    numbers = [num1 + i * num2 for i in range(length)]
    index = random.randint(0, 9)
    correct_answer = numbers[index]
    numbers[index] = ".."
    question = ' '.join(map(str, numbers))
    print(f"Question: {question}")
    return correct_answer


def main():
    name = welcome_user()
    print(PROGRESSION)
    correct_answers = 0
    while correct_answers < 3:
        correct_answer = get_question()
        answer = input('Your answer: ')
        if int(answer) == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            correct_answers = 0
            print(f"{answer} i{WRONG_ANSWER} {correct_answer}.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
