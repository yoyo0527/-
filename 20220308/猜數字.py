q='1758'
ans='7358'
a=0
b=0
for i in range(0,4):
    if q[i]==ans[i]:
        a+=1
    elif q[i]!=ans[i] and q.count(ans[i])>0:
        b+=1
print(a,"A",b,"B")