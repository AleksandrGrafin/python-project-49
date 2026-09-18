from brain_games.games.brain_progression import INSTRUCTION, question_answer
from brain_games.games.engine import start_game


def main():
    start_game(INSTRUCTION, question_answer)


if __name__ == '__main__':
    main()

