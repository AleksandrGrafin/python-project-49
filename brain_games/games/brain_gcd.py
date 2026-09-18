import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def question_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'{x}, {y}'        
    
    if x > y:
        x %= y
    else:
        y %= x
    correct_answer = x or y 
    return question, str(correct_answer)
