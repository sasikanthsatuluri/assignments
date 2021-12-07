print("--------------------------------")
print("NOW EMPLOYEE")
print("--------------------------------")
name = str(input('enter the name:'))
eid = int(input('enter the id .no:'))
amount =[]
expenses=[]
hr = int(input('input hr amount:'))
basic = int(input('enter the basic amount:'))
special = int(input('enter the special amount:'))
tax = int(input('enter the tax amount:'))
netamount = (hr+basic+special)-tax
amount.append(netamount)
print('the net amount is:',netamount)
print("--------------------------------")
print("NOW EXPENDITURE")
print("--------------------------------")
no_of_months = int(input("Enter no of months : "))
total_expenditure = 0
for month in range(no_of_months):
    print("-----------------------------------------")
    name = input("Enter name of month : ")
    print("-----------------------------------------")
    no_of_expenditure = int(input("Enter no of expenditure : "))
    expenditure = {}
    for i in range(no_of_expenditure):
        name_of_expenditure = input("Enter name of expenditure : ")
        amount_of_expenditure = int(input("Enter amount of expenditure : "))
        total_expenditure += amount_of_expenditure
        expenditure[name_of_expenditure] = amount_of_expenditure
        print("For month : ",name)
        print("--------------------------------------")
        print(expenditure)

    print("-----------------------------------------")
print("TOTAL EXPENDITURE = ",total_expenditure)
print("-----------------------------------------")

net_savings = (netamount*no_of_months) - total_expenditure
if(net_savings >= 0):
    print("-----------------------------------------")
    print("WINNER")
    print("-----------------------------------------")
else:
    print("-----------------------------------------")
    print("LOSER")
    print("-----------------------------------------")



