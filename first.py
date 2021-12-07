'''p1 = [1,2,3,4]
p2 = [2,3,4,5]
r1 =[i for i in p1 if i not in p2]
r2 =[j for j in p2 if j not in p1]
print(r1+r2)''


'''l1 = set([1,2,3,4,5,6,7])
l2 = set([9, 8, 10, 1,2])
print(l1.symmetric_difference(l2))

l1 = set([1,2,3,4,5,6,7])
l2 = set([9, 8, 10, 1,2])
print ([i for i in l1 if str(i) not in ''.join([str(i)for i in l2])]+[j for j in l2 if str(j) not in ''.join([str(j)for j in l1])])


l1 =  [1,2,3]
for i in l1:
    print(str(i))'''

'''def sub(a,b):
    c = a-b
    return c
z = sub(10,5)
print('difference:',z)
z= sub(100,90)
print(z)

def app(a,b):
    a.append(b)
    return a
c= app(list(range(3)),8)
print('result:',c)
c= app([1,2,4],9)
print(c)'''


'''def febo(a,f,s):
    if (a<=0):
        print('the requested is in \n',f)
    else:
        print(f,s,end=' ')
        for x in range(2,a):
            next = f+s
            print(next,end=' ')
            f=s
            s=next
        return a,f,s
  febo(5,1,1)'''



'''print('----------febo-------------')
def recr_febo(n):
    if n<=1:
        return n
    else:
        return(recr_febo(n-1)+recr_febo(n-2))

terms = int(input('enter the number of terms'))
if terms<=0:
    print('enter a positive value')
else:
    for i in range(terms):
        print(recr_febo(i))'''



num1 = int(input('enter the number:'))
num2 = int(input('enter the number:'))
count= num1
while count<=num2:
    if count%5==0 and count%7==0:
        print('the number is divisable by both 5 and 7',count)
        count=count+1























