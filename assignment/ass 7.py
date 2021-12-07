a = int(input('enter the number :'))
b = int(input('enter the number :'))
print('sum is :',a+b)
print('difference b/w b and a :',b-a)
print('product is ',a*b)
print('quotient', a/b)
print('remainder', a%b)
from math import log10
print('result of log10',log10(a))
print('result of ab',a**b)

def numbers(a,b):
    print('sum is :', a + b)
    print('difference b/w b and a :', b - a)
    print('product is ', a * b)
    print('quotient', a / b)
    print('remainder', a % b)
    from math import log10
    print('result of log10', log10(a))
    print('result of ab', a ** b)
    a = int(input('enter the number :'))
    b = int(input('enter the number :'))
    numbers(a, b)