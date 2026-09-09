import random
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print ('Find the greatest common divisor of given numbers.')
    wins = 0
  
    while wins < 3:
        a = random.randint (-100, 100)
        b = random.randint (-100, 100)
        x = abs(a)
        y = abs(b)
        print (f'Qwestion:{x}, {y}')

        while x !=0 and y !=0:
            if x>y:
                x%=y
            else:
                y%=x
            correct_answer = x or y 
    
            user_anwer = int(input('Your answer:'))

            if user_anwer == correct_answer:
                wins += 1
                print ('Correct!')
            else:
                print (
                    f"Your answer:'{user_anwer}' is wrong answer ;(." 
                    f"Correct answer was '{correct_answer}'. \n"
                    f"Let's try again, {name}!"
                )
                return

            print ('Congratulations, {name}!')
            
if __name__ == '__main__':
    main()
