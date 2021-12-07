class Job:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
        print("NOW EMPLOYEE")
    def earning(self):
        amount = []
        hr= int(input('enter the hr amount:'))
        basic = int(input('enter the basic amount:'))
        special = int(input('enter the special amount:'))
        tax = int(input('enter the tax amount:'))
        netamount = (hr + basic + special) - tax
        amount.append(netamount)
        print('the net amount is:', amount)
        months = int(input('enter the no.of months:'))
        total_expenditure =0
        for j in range(months):
            month_name = input('enter the name of the month:')
            expenditure_val = int(input("Enter no of expenditure : "))
            expenditure = {}
        for i in range(expenditure_val):
            name_of_expenditure = input("Enter name of expenditure : ")
            amount_of_expenditure = int(input("Enter amount of expenditure : "))
            total_expenditure += amount_of_expenditure
            expenditure[name_of_expenditure] = amount_of_expenditure
            print("For month : ", month_name)
            print(expenditure)
            print("TOTAL EXPENDITURE = ", total_expenditure)
        net_savings = (netamount * months) - total_expenditure
        if (net_savings >= 0):
            print("WINNER")
        else:
            print("LOSER")

person = Job("sasikanth",1322)
print(person.name)
print(person.earning())

