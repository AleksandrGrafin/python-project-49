from brain_games.cli import welcome_user


def start_game(instruction, question_answer):
    name = welcome_user()
    print (instruction)
    
    wins_count = 3
    
    for _ in range (wins_count):
        question, correct_answer = question_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer ==str(correct_answer):
           print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"\nCorrect answer was '{correct_answer}.'"
                f"\nLet's try again, {name}!"
                )
            break
    else:
        print (f'Congratulations, {name}!')
