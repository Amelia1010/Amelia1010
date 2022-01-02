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