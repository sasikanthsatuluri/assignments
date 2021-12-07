n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)

def positive(n):
    sum = (n * (n + 1)) / 2
    print("Sum of the first", n ,"positive integers:",sum)
    n = int(input("Input a number: "))
    positive(n)