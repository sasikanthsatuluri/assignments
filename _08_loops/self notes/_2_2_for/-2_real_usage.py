list1= [1,2,3]
list2= [2,3,4]
for i in list1:
    if i in list2:
        print('some matching',i)
    else:
        print('not matching',i)
