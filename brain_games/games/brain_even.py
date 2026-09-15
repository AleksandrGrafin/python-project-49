import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def question_answer():
    i = random.randint(1, 100)
    if i % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = str(i)
    return question, correct_answer
