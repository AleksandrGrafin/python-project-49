
import random

from brain_games.cli import welcome_user


def main():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no"')

    wins = 0
    correct_answer = ""

    while wins < 3:
        i = random.randint(1, 100)
        print(f"Question: {i}")

        is_even = (i % 2 == 0)

        user_answer = input("answer: yes/no:").strip().lower()

        if is_even:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            wins += 1
            print('Correct!')
        else:
            print(
                f'"{user_answer} is wrong answer ;(.'
                f'Correct was {correct_answer}"'
            )
            break

    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
