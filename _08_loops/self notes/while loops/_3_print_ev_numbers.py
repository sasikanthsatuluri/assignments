print('--even numbers using while loop--')
n = 1
while n<10:
    if n%2==0:
        print(n)
    n+=1

print('-- odd numbers using while loop--')
m = 1
while m<10:
    if m%2==1:
        print(m)
    m = m+1

print('all possible numbers divisable by 2 and 3')
p = 1
while p<20:
    if p%2==0 and p%3==0:
        print(p)
    p+=1




