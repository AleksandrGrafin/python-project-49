import random
from brain_games.cli import welcome_user

def is_prime(number):
    
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range (3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
         

def main():
    
    
    name = welcome_user()
    
    print ('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    wins = 0
    
    while wins < 3:
        
        number = random.randint(1, 100)
    
        print (f'Question: {number}')
        
        correct_answer = 'yes' if is_prime(number) else 'no'
            
        user_answer = input('Answer: ').strip().lower()
        
        if user_answer == correct_answer:
            wins += 1
            print ('Correct!')
        else:
            print (
                f'"{user_answer}" is wrong answer ;(.'
                f' Correct answer was "{correct_answer}".'
                f"\nLet's try again {name}!"
                )
            break
    else:
        print (f'Congratulations, {name}!')


if __name__ == '__main__':
    main()


