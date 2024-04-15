
import random
#a=int(input('Enter any Number Between 1 to 10'))
b=random.randint(1,10)
print(b)
c=5
for i in range(1,6):
    a=int(input('Enter any Number Between 1 to 10\n'))
    if a==b:
        print('You Won')
        break
    else:
        print('You Lost')
        print('You have only ',c-1,' Chance Left')
        c=c-1
if a==b:
    pass
else:
    print('you Lost The number was',b,'')