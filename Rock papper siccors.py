import random

computer_choice = random.randint(1,3)
user_choice = int(input('Do you want - rock, paper, or scissors? 1 for rock, 2 for paper and 3 for sicssors\n'))
user_score = 0
computer_score = 0
tie = 0


if computer_choice == user_choice:
    print('tie')
    tie = tie+1
    

elif  user_choice == 1  and computer_choice == 3:
    print('WIN')
    user_choice = user_choice+1

elif  user_choice == 3 and computer_choice == 1:
    print("Win!")
    user_choice = user_choice+1

elif user_choice == 2  and computer_choice == 3 :
    print('Win')
    user_choice = user_choice+1
else: 
    print ('You lose and the computer wins')
    computer_score = computer_score+1

again = input('do you want to play again?\n')

while again=='yes':
    computer_choice = random.randint(1,3)
    user_choice = int(input('Do you want - rock, paper, or scissors? 1 for rock, 2 for paper and 3 for sicssors\n'))
    again = input('do you want to play again?\n')

if tie == 1:
    print (f'you win {user_score} times and computer win {computer_score} time and there were {tie} tie')

elif tie!= 1:
    print(f' You win {user_score} times and computer wins {computer_score} times and there were {tie} ties')




