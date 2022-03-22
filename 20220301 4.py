sum=0
for i in range(1,11):
    if i%2==0:
        sum-=1/i
    else:
        sum+=1/i
print(sum)