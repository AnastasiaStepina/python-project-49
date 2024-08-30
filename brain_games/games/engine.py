import prompt
from brain_games.games.const import COUNT_ROUNDS, WELCOME
WRONG_ANSWER = 'is wrong answer ;(. Correct answer was'


def welcome_user():
    name = prompt.string(WELCOME)
    print(f"Hello, {name}!")
    return name


def get_enginie(game):
    name = welcome_user()
    print(game.RULES)
    correct_answers = 0
    while correct_answers < COUNT_ROUNDS:
        question, correct_answer = game.get_question()
        print(question)
        answer = input('Your answer: ')
        if answer == correct_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(f"{answer} {WRONG_ANSWER} {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    get_enginie()
