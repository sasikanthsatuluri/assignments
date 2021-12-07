# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
''''if __name__ == '__main__':
    print_hi('PyCharm')'''''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



'''a = 'sasikanth'
for i in a:
    print(p)'''

'''a = ['my', 'name','is' 'sasikanth']
for i in a:
    for j in i:
        print(j)'''

'''a = [ 'age','eid','salary']
b = [27, 1322, 90000]
c = dict(zip(a,b))
print(c)
print(c.values())'''

'''def person():
    name = str(input('enter the name:'))
    if name:
        print("hi\t"+ str(name))
    else:
        print("hello")
    return name
p = person()
print('my name is\t'+p)'''

'''def my_func():
    name = str(input('enter the process:'))
    print('the  operation  is\t'+str(name))
my_func()'''

# if we donot know how many augments will be passed into the parameter then use * before that

'''def children(*name):
    print('the children names '+name[0])
children('sasi','kanth','bhavya')'''

'''def children(**name):
    print('the children names '+name['last'])
children(first='sasi',last='kanth')'''

'''def recr(n):# function calling the function itself is a recursive function
    if n>0:
        result = n+recr(n-1)
        print(result)
    else:
        result =0
    return result

recr(20)'''

''''def my_place(native='bhimavaram'):
    print(' i am from '+ native)
my_place()
my_place('gulf')# if we assign any argument in to the parameter other than assigned argument then function if we call it takes
                #--  given argument rather than previously assigned argument for that parameter'''

# program to find the how many zeros at the end of given posititve integer factorial
def factorial(n):
    p = n//5
    q = p
    while p>0:
        p = p/5
        q = q+int(p)
    return q
print(factorial(20))





