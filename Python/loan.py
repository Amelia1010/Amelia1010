money_owed =float(input('How much do you owe, in dollors\n'))

payment = float(input('What will your monthly paument be\n'))
months = int(input('How many muths do you want to see resultys for\n'))

#Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months): 
#Add in intrest 
    intrest_paid= money_owed * monthly_rate
money_owed= money_owed + intrest_paid
if (money_owed - payment < 0):
    print('the last payment is', money_owed)
    print('you paid of the loa in', i+1, months)
    break
#make payment
money_owed = money_owed- payment

#print the results 
print('Paid' , payment, 'of which', intrest_paid, 'was intrest', end= ' ')
print('Now I owe', money_owed)

