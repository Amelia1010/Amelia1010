items = { ' Chess board' : 50,
                'Milk': 15,
                'Egg': 60,
                'Plants': 23,
                'Diamonds': 3000000,
                'Towels': 50,
                'Chair' : 500000,
                'Mouse': 15000,
                ' Dictionary':  50
                }
for i in items:
    print ( ' we have: '+ i)

purchase = input(' soo, What would you like to buy today?\n') 
while purchase not in  items:
    print('We do not have that rn we will get it after a decade or so, after all patiance is the key for many things')
    purchase = input('What else would u like to buy\n')

Price = 0
total = 0

mina = input(' Would you like to buy anything else?\n')

Price= items.get(purchase)
total = total+Price

while mina=='yes':
    purchase= input('what else would you like to buy\n')
    while purchase not in  items:
        print('We do not have that rn we will get it after a decade or so, after all patiance is the key for many things')
        purchase = input('What else would u like to buy\n')
    mina = input('would you like to buy anything else?\n ')                                                                                                                                        
    Price= items.get(purchase)
    total = total+Price


print (f'You bought: {purchase} and {purchase}') 
print(f'You spent: {total} dollars ')
print("Thank you for shopping at Wallmart!\n and don't forget to thank Mina")
