print('welcom to sbi bank')
print('insert the card ')
langude=input("enter language: ")
if langude =='english':
    print('english ')
elif langude=='telugu':
    print('telugu ')
else:
    print('tamil ')
pin=int(input('enter pin number: '))
print('select options')
option=input(' DEBOSIT AND WITHDRAW  ')
if option=='DEBOGIT':
    print('open depo ')
    enter=int(input('enter amount: '))
    if enter > 2000000:
        print('over amount ')
    else:
        print('amount deposited successfully')
        print('debosit done ')
else :
    print('open withdraw')
    enter=int(input('enter amount: '))
    if enter > 2000000:
        print('over amount ')
    else:
        print('amount withdrawn successfully')
        print('withdraw done  ')
print('thank you for using sbi bank')
print('please collect your card ')
print('WELCOME BACK')

    



