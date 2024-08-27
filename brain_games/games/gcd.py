import random
from brain_games.games.even import welcome_user
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER, WRONG_ANSWER, GCD


def get_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {num1}  {num2}")
    return num1, num2


def get_gcd(num1, num2):
    while num2 != 0:
        num2, num1 = num1 % num2, num2
    return num1


def main():
    name = welcome_user()
    print(GCD)
    correct_answers = 0
    while correct_answers < 3:
        num1, num2 = get_question()
        answer = input('Your answer: ')
        correct_answer = get_gcd(num1, num2)
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
