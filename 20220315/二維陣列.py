grade=[[96,65,73],[88,76,82]]
a=b=c=0
for i in range(len(grade)):
    a+=grade[i][0]
    b+=grade[i][1]
    c+=grade[i][2]
print("國文平均:",a/2)
print("英文平均:",b/2)
print("數學平均:",c/2)
