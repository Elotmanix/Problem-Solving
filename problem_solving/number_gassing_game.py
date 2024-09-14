import random

number_to_guess = random.randint(1,100)
while True: 
    try:   
        guess = int(input('Guess the number between 0 and 100 : '))
        if guess > number_to_guess : 
            print('too high')
        elif guess < number_to_guess : 
            print('too low')
        else: 
            print('Congratulations you guessed the number')
            break
    except ValueError :
        print('Please enter a number')

        