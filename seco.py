'''a= [1,2,3]
b= [2,3,4]
c = set(set(a)-set(b))
d = set(set(b)-set(a))
print(c)
print(d)'''

#def print_hi(name):
  #  print(f'hi {name}')
#name =input('enter the name')
#print_hi(name)



'''num = int(input('enter the number '))
if num>= 10:
    if num%10==0:
        print('its the req one')
    else:
        print('no')'''


'''

a = int(input('enter the value of a'))
b = int(input('enter the value of b'))
if a > b and a % 2 ==0:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else :
    print('nothing')
    '''

'''a = int(input('enter the value'))
if not a/2 == 7:
    print('here is the number')
else:
    print ('the number')
    '''

''''x = int(input('enter the number x'))
p = int(input('enter the number p'))
q = int(input('enter the number q'))
if p<=x<=q:
    print('it is in between')
elif p<x>=q:
    print('x is greater than q')
elif p>=x<q:
    print('x is greater tha p but less than q')
else :
    print('no')'''''

'''p = int(input('enter the number '))
if p>=10 or p+2==10:
    print('condition satisfied')
elif p==11:
    print('next one')
else:
    print('this is neither')'''


'''for x in range(1,11):
    for y in range(x):
         print('*',end=" ")
    print("\n")'''

'''list1 =[1,2,3]
list2 =[2,3,4]
print(set(zip(list1,list2)))'''     #a tuple is created by zipping the values of both lists

'''n = 10
total_numbers = n
sum = 0
while n >= 0:
    sum += n
    n -= 1
print("sum =", sum)

average = sum / total_numbers
print("Average = ", average)'''

'''num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))'''

'''multiply = 1
values = [8,16,22,12,41]
n = len(values)

for i in values:
    multiply = (multiply)*(i)

geometricMean = (multiply)**(1/n)
print ('The Geometric Mean is: ' + str(geometricMean)) '''

'''

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)'''