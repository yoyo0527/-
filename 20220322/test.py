a="c1101561"
d=[]
for i in range(1,57):
    d.append(a+"{0:02d}".format(i))

import random
grade=[]
for i in range(1,57):
    grade.append(random.randint(0,100))

b={"c110156132":60}
print(b["c110156132"])
b["c110156133"]=99