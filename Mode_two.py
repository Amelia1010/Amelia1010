from types import EllipsisType
from colorama import Fore, Back, Style
print(Fore.LIGHTGREEN_EX)
foobar = int( input('Give me a interger\n'))
#We ask for a number ^^ 
print(Fore.LIGHTCYAN_EX)
#Here is what we want to do with the number:
i = 0

while i<=foobar:
    if  i  %2==0:
        print (i )
    i=i+1

print('end')