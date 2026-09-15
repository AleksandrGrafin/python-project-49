import random

INSTRUCTION = 'What is the result of the exppression?'

def question_answer():
    i = random.randint (1, 100)
    b = random.randint (1, 100)
    signs = ['+' , '-' , '*']
    sig =  random.choice(signs)
    question = f'{i} {sig} {b}'

    if sig == '+':
        correct_answer = i + b
    elif sig == '-':
        correct_answer = i - b
    elif sig == '*':
        correct_answer = i * b
  
    return question,str(correct_answer)
