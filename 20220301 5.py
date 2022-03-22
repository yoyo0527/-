sum=1
for i in range(1,10):
    if i%2==0:
        sum+=i/(i+1)
    else:
        sum-=i/(i+1)
print(sum)