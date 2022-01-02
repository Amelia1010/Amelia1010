import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess=  int(input(f'Guess a random number between 1 and {x}:\n  '))

        if guess < random_number:
            print('Sorry guess again. Too low')

        elif guess >  random_number:
            print('Sorry guess again. too high')
    
    else:
     print(f'Yay!!!!!!!!!  You have guessed number {guess} right. You are in the goldilocks zone!!!!!!!!!!!!!!!!!!!')

guess(5)



if guess(x):
    low = 1
    high = x
    feedback = ' '

    while feedback != 'c':
        if low!= high:
            guess = random.randint(low,high)

        else:
                guess = low
                guess = random.randint(low.high)
                feedback = input ( ' is {guess) too high ( H), too low (L), or correct (C)')
        if feedback == 'h':
             high = guess-1

        elif feedback == 'l' :
            low = guess +1

    print ('high')

guess(10)
