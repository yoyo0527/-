low=100
a=[60,70,35,55,90]
x=0
for i in range(len(a)):
    if low>a[i]:
        low=a[i]
for i in range(len(a)):   
    if low==a[i]:
        break
print("第",i+1,"位同學最低分")