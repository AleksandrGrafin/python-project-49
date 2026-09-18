import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def question_answer():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    x = abs(a)
    y = abs(b)
    question = f'Qwestion:{x}, {y}'        
    
    if x > y:
        x %= y
    else:
        y %= x
    correct_answer = x or y 
    return question, str(correct_answer)
