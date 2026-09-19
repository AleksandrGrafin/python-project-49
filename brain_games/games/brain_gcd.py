import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'

    x = num1
    y = num2
    while y != 0:
        x, y = y, x % y
    correct_answer = x
    return question, str(correct_answer)        
    
