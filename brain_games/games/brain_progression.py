import random

INSTRUCTION = 'What number is missing in the progression?'


def question_answer():
    start = random.randint(3, 8)
    length = 10
    hidden_index = random.randint(4, length - 2)
    step = random.randint(3, 5)
    spisok = []
    correct_answer = 0
    
    for i in range(length):
        value = start + i * step
        
        if i == hidden_index:
            spisok.append('..')
            correct_answer = value
            
        else:
            spisok.append(value)
            
    question = ' '.join(map(str, spisok))
    
    return question, correct_answer
