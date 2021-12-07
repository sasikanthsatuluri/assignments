print("Enter Number of Subjects: ")
subNo = int(input())
print("Enter Marks Obtained in " + str(subNo) + " Subjects: ")
mark=[]
tot = 0
for i in range(subNo):
    mark.append(input())
sub = ['eng','tel','hin','sci','soc','mat']
sub_marks =dict(zip(sub,mark))
print(sub_marks)
for i in range(subNo):
    tot = tot + int(mark[i])
    avg = tot / subNo
print('the average marks of all subjects is :',avg)
if avg > 90:
    print('distinction')
if 75 < avg < 90:
    print('average score')
avg3 = (mark[0] + mark[1] + marks[2]) / 3
if avg < 75:
 if avg3 < 75:
     print('chance to be given')

