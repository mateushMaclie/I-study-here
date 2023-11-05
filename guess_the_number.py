import random

def number_generator():
    number=random.randint(1000,9999)
    return number


def guess_func(num,gues):
    number_=[int(x) for x in str(num)] #спизидл у гпт
    guess_=[int(x) for x in str(gues)] 

    a='' 
    for i in range(len(number_)):
        if number_[i] == guess_[i] :
            a+='+'
        elif number_[i] in guess_:
            a+='!'    
        else:
            a+='-'
    return(a)

#эту часть тож
num=number_generator()
while True:
    gues=int(input())
   
    if gues == num:
        print('ti ygagdal')
        break
    
    a=guess_func(num,gues)
    print(a)   
