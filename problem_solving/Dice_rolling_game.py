import random

'''choice = input("Roll the dice? (y/n):").lower()
while choice != 'n':   
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if choice == 'y':
        print(f'the random numbers are: {(die1, die2)}')
        choice = input("Roll the dice? y/n:")
    else:
        print('sorry, invalid input')
        choice = input("Roll the dice? y/n:")

if choice == 'n':
    print('thanks for playing')  

'''
while True:
    choice = input("Roll the dice? (y/n):").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'the random numbers are: {(die1, die2)}')
        print(f'Your scor is: {die1 + die2}') #added score calculation
    elif choice == 'n':
        print('thanks for playing')
        break
    else:
        print('sorry, invalid input')
       