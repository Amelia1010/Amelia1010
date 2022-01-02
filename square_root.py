# we need to import math function that can do the math for us
import math
#Ask for values and oprations 
opration=input('Do you want square of that number or the square root? type s sqaure and sqrt for square root\n')
from typing import is_typeddict
from colorama import Fore, Back, Style

while opration not in ('s' or 'sqrt') :
    opration=input('Do you want square of that number or the square root? type s sqaure and sqrt for square root\n')


foobar = int(input("Give me a number\n"))

if opration=='s':
    print(foobar*foobar)


elif opration=='sqrt':
    res = math. sqrt(foobar)
    print(res)


    
