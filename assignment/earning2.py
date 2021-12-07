nameoftheemp = str(input('enter the name:'))
eid = int(input('enter the id :'))
hr = int(input('input hr amount:'))
basic = int(input('enter the basic amount:'))
special = int(input('enter the special amount:'))
tax = int(input('enter the tax amount:'))
netamount = (hr+basic+special)-tax
print('the net amount is:',netamount)
print("--------------------------------")
no_of_months = 0
total_expenditure=0
while(True):
    month=input('enter the name of the month:')
    no_of_months+=1
    while(True):
        expenditure= input('enter the name of the expenditure:')
        amount = int(input('enter the expenditure amount:'))
        total_expenditure+=amount
        if((input('want to enter another expenditure(yes/no):'))=='yes'):
            continue
        else:
             break
    if((input('want to enter another month (yes/no):'))=='yes'):
        continue
    else:
         break
savings = (netamount*no_of_months)-total_expenditure
print('total amount in monthly:',netamount)
print('total expenditure of all months:',total_expenditure)
print('savings:',savings)




