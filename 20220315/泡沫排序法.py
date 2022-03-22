a=[60,70,35,55,90]
b=[0,0,0,0,90]
s=0
while s<2:
    for i in range(0,4): 
        if a[i]>a[i+1]:
            b[i]=a[i+1]
            b[i+1]=a[i]
            a[i]=b[i]
            a[i+1]=b[i+1]           
        elif a[i]<a[i+1]:
            b[i]=a[i]
    s+=1                   
print(a)