'''
syntax of for loop:
for [varaible (any)] in range(number of items in the sequence):
if there is list of numbers or 'string'
SYNTAX: for(variable) in 'list' or 'string
'''

'''message = "Hello sasikanth"
for name in message:
    for val in name:
        print(val)'''

emp_details = {'eid' :1322 ,'name' :'sasikanth' ,'sal' :100000}
for key ,val in emp_details.items():
    print(key ," : ", val) # printing keys along with values in the dictionary

for key, val in emp_details.items():
        print(key, " : ", val)

for key in emp_details.keys():
            print(key)
for val in emp_details.values():
           print(val)

