import random
from brain_games.games.even import welcome_user
from brain_games.games.const import MIN_NUMBER, MAX_NUMBER, WRONG_ANSWER, PRIME


def get_question():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {num}")
    return num


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def main():
    name = welcome_user()
    print(PRIME)
    correct_answers = 0
    while correct_answers < 3:
        num = get_question()
        answer = input('Your answer: ')
        if (answer == 'yes' and is_prime(num)
                or answer == 'no' and not is_prime(num)):
            correct_answers += 1
            print("Correct!")
        else:
            correct_answers = 0
            correct_answer = 'yes' if is_prime(num) else 'no'
            print(f"{answer} {WRONG_ANSWER} {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
