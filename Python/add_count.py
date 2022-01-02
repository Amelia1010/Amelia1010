#Change the color to the contrast color for your theme so it is clearer to see
from colorama import Fore, Back, Style
print(Fore.WHITE)

#Number output
number = int(input('give me a number between one to ten\n'))

#Variables
sum = 0
i=0

while i <= number:
    sum = sum + i
    i= i+1

print (sum)
