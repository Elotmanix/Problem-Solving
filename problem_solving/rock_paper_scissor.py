import random

emojis = {'r':'🧱','p':'📃','s':'✂'}
choices = ('r','p','s')

while True:   
    user_choice = input('Enter rock paper scissor (r/p/s) : ').lower()
    if user_choice not in choices : 
        print ('Invalid input')
        continue

    computer_choice = random.choice(choices)

    print (f'you choose {emojis[user_choice]} ')
    print(f'computer choose {emojis[computer_choice]} ')

    if user_choice == computer_choice:
        print ('Tie!!')
    elif ((user_choice == 's' and computer_choice == 'p') or 
         (user_choice == 'p' and computer_choice == 'r') or 
         (user_choice == 'r' and computer_choice == 's')):
        print("You win!")     
    else : 
        print ('you lose')

    Continue = input('Continue? (y/n): ').lower()
    if Continue != 'y' and Continue != 'n': 
        print ('Invalid input')
        Continue = input('Continue? (y/n): ').lower()
    elif Continue == 'y':
        continue
    elif Continue == 'n':
        break

