import random
# def guess(x):
#     random_numbers=random.randint(1,x)
#     guess=0
#     while guess!=random_numbers:
#         guess=int(input('guess a number'))
#         if guess<random_numbers:
#            print('sorry,guess too low.')
#         elif guess >random_numbers:
#             print('sorry,guess to high')
#     print('congrualations.you guessed the random number{random_numbers}')
# print(guess(50))

import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        if high != low:
            guess=random.randint(low,high   )
        else:
            guess=low
        feedback=input(f'is {guess} too high(H),too low(l),or correct(C)').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'congratulation you guessed your number {guess},correctly')
computer_guess(500)