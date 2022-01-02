
#Change colors!
from colorama import Fore, Back, Style


#Our first variable in the world!!
number1=  float (input('Give me a number\n'))

#Our second variable in the world!!!
print(Fore.MAGENTA)
#Change colors ^^^^^^^^^^
number2= float(input('Give me another number\n'))

# More variables!!!
#Variables for oprations, YAY!!!!!!!!!!!!
print(Fore.GREEN)
operation= input('Do you want me to add, subtract or multiply it\n')

#Enough variables

#Cuz it's the:
#Time.......To........Code.......With........If statements
if operation== 'add':
    print(Fore.RED)
    print (  number1+number2)

elif operation== 'subtract':
    print(Fore.CYAN)
    print ( number1 - number2)

elif operation =='multiply':
    print(Fore.BLUE)
    print(number1*number2)

else:
    print('Sorry but I cannot do that')  

print(Fore.WHITE)

#Always execute with the contrast color of your theme


#Problem:
#   How do we subtract?
#   How do I convert string to intager or float

#Solutions
#For answers go to problems_solutions page and see for yourself