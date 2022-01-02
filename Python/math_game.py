import random

first_number = random.randint(9,100)
second_number= random.randint(9,100)

question = int(input(f' {first_number} + {second_number}\n'))
answer = first_number+second_number

right_answer = 0
wrong_answer = 0

total_question = 0

if question == answer:
    print('great!, You got this one right keep going')
    right_answer=right_answer+1
    another_question = input('would you like another question?\n')
    total_question=total_question+1

elif question!=answer:
    print(f'oops!, You got it wrong, the answer is {answer} try getting the next one right\n')
    wrong_answer=wrong_answer+1
    another_question = input('would you like another question?\n')
    total_question=total_question+1


while another_question == 'yes':
    first_number2 = random.randint(9,100)
    second_number2 = random.randint(9,100)
    question = int(input(f'{first_number2} + {second_number2}\n'))
    answer = first_number2+second_number2
    if question == answer:
        print('great!, You got this one right keep going')
        right_answer=right_answer+1
        another_question = input('would you like another question?\n')
        total_question=total_question+1
    elif question!=answer:
        print(f'oops!, You got it wrong, the answer is {answer} try getting the next one right\n')
        wrong_answer=wrong_answer+1
        another_question = input('would you like another question?\n')
        total_question=total_question+1
        another_question = input('would you like another question?\n')

if right_answer==1:
    print(f' you got {right_answer} question right and {wrong_answer} questions wrong out of {total_question} questions')

elif wrong_answer ==1:
    print(f' you got {right_answer} questions right and {wrong_answer} question wrong out of {total_question} questions')


else:
    print(f'you got {right_answer} questions right and {wrong_answer} questions wrong out of {total_question}  questions')