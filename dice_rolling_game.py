import random
#we can create the variable to functioning the loop
#intead we can use direct True to function

while True:
    choice=input('Roll the dice (y/n):').lower() #it automatically change the letter to lowercase ,if the  user enter the uppercase
    if choice=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif choice=='n':
        print('Thanking you for playing!')
        break
    else:
        print('Invalid choice')