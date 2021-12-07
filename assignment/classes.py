class Dict_a:
    def __init__(self,dict1):
        self.id = dict1[1]['id']
        self.name = dict1[1]['name']
        self.salary = dict1[1]['salary']
        for key in dict1:
            if key%2==0:
                print("even number:",dict1[key])
    def emp_details(self):
        return dict1.values()
    def emp_salary(self):
        net = 0
        for i in self.salary.values():
#            print(i)
            net = net+i
        print("total salary of emp:",net)
dict1= {1:{'id':101,'name':'john','salary':{'BS':100,'SA':1000,'HR':5000}},2:{'id':102,'name':'kevin','salary':{'BS':200,'SA':2000,'HR':6000}}}
result = Dict_a(dict1)
print("Employee Details:",result.emp_details())
result.emp_salary()

class Dict_b:

    def __init__(self, dict2):
               self.id =dict2[1]['id']
               self.firstname=dict2[1]['firstname']
               self.seconame=dict2[1]['seconame']
               self.location=dict2[1]['location']
               self.salary = dict2[1]['salary']
               for key2 in dict2:
                   if key2%2==0:
                       print("even number:",dict2[key2])

    def emp_details(self):
        return dict2.values()

    def emp_salary(self):
            nett = 0
            for i in self.salary.values():
             nett = nett + i
            if nett>10000:
                    print('the salary is 10k',nett)
            else:
                    print('the salary is not in range')



dict2 = {1: {'id': 2424, 'firstname': 'ravi', 'seconame': 'chandra', 'location': 'bvrm',
                 'salary': {'BS': 200, 'SA': 1500, 'HR': 2000},
                 2: {'id':4242,'firstname': 'siva', 'seconame': 'ram','location':'plkl','salary': {'BS': 400, 'SA': 2000, 'HR': 6000}}}}
result = Dict_b(dict2)
print("Employee Details:", result.emp_details())
result.emp_salary()






