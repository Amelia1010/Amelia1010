#Variable that asks for the stoping  point
from typing import is_typeddict
from colorama import Fore, Back, Style

starting_point= int(input('Give me a starting point\n'))
ending_point = int(input('Give me a stoping point\n'))

#A random number to make things easier
while starting_point>ending_point:
    print( "enter again, and double check the value"  )
    print(Fore.RED)
    enter_again = input('Which value would u like to enter again? a for strarting and b for ending and c for both \n ')


    if enter_again=='a':
        starting_point=int(input('Give me another starting point \n'))
    elif enter_again=='b':
        ending_point=int(input('Give me another ending point\n'))
    elif enter_again =='c':
        starting_point=int((input('give me another starting point\n')))
        ending_point=int(input('Give me another ending point\n'))


# user is sometimes nice to us
while starting_point<=ending_point:
    if starting_point%2==0:
        print(f'{starting_point} is a even number')
    
    else:
        print(f'{starting_point} is a odd number')
    
    starting_point=starting_point+1