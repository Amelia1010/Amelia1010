import random
game = input('Do you want to play flip  a coin?\n')
IWin = 0
YouWin=0
total = 0

while game == 'yes':
    answer = int(input('Do you want heads and tails? 1 for heads and 2 for tails \n'))
    coin = random.randint(1,2)
    if answer==coin:
        print('Good jOb You WIN!!!!')
        IWin=IWin+1
        total=total+1
        
    else:
        print('I win and You LOSE!!! HAAHAHAHAHAHAHAHAHA')
    game = input('do you want to play again?\n')
    YouWin=YouWin+1
    total=total+1

if game == 'no':
    print('ok fine, maybe later')
    print(f'You win {IWin} times')
    print(f'I win {YouWin} times')
    print(f'we played a total of {total} games')
