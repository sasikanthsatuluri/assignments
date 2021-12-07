''''num = 1
while num<=5:
    print(num)
    num+=1
print('out of the loop') ''' #simple while loop


'''num = int(input('enter the value:'))
while num<=8:
    print(num)
    num+=1
    if num==6:
        break''' # if condition within while loop

'''
a =1
while a < 20:
    if a%2==0:
        print(a)
    a = a+1''' #printing even numbers

'''a =1
while a < 20:
    if a%3==0:
        print(a)
    a = a+1'''# multiples of 3, like this we can also print for multiples of 5 even

''''lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)'''''  #printing prime numbers by for loop


'''a = 0
while a<6:
     a= a+1
     if a==3:
        continue
     print('----------',a)'''

'''a = 0
while a<6:
    print(a)
    a+=1
    if a==5:
        break''' #prints from  0 t0 4


'''a = 0
while a<6:
   a+=1
    if a==5:
        break
          print(a)'''#prints from 1to 4




