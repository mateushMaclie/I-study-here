import random
number=random.randint(1000,9999)
print(number)
while True:
    guess=int(input())

    if guess==number:
        print('ты угадал!')

    number_=[]
    for num in str(number):
        number_.append(num)
    print(number_)


    guess_=[]
    for digit in str(guess):
        guess_.append(digit)
    print(guess_)



    a='' 
    for i in range(len(number_)):
        if number_[i] == guess_[i] :
            a+='+'
        elif number_[i] in guess_:
            a+='!'    
        else:
            a+='-'
    print(a)

    
