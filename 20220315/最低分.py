low=100
a=[60,70,35,55,90]
for i in range(len(a)):
    if low>a[i]:
        low=a[i]
print(low)