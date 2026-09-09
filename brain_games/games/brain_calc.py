import random
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print ('What is the result of the expression?')
    wins = 0
    
    signs =['+', '-', '*']
    random.shuffle(signs)

    while wins <3:
        i = random.randint (1, 100)
        b = random.randint (1, 100)
        sig = signs[wins]
        print (f'Question:{i} {sig} {b}')
        
        if sig == '+':
            correct_answer = i + b 
        elif sig == '-':
             correct_answer =i - b 
        elif sig=='*':
            correct_answer = i*b 
                
        user_answer = int(input ('answer:'))
            
        if user_answer == correct_answer:
            wins +=1
            print ("Correct!")
        
        else:
            print (
                f'{user_answer} is wrong answer ;(.'
                f' Correct answer was {correct_answer}'
                f"let's try again {name}!"
            )
            break
            
    else:
        print (f'Congratulations, {name}!')
                
if __name__ == '__main__':
    main()
