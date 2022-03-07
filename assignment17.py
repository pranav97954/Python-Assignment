"""
#Q1.
t1=10,20,30,40,50,60
c=0
for e in t1:
    c+=1
print(c)
#Q2.
t1=10,20,30,40,50,60
i=-1
while(i!=-len(t1)):
    print(t1[i],end=",")
    i-=1
if(i==-len(t1)):
    print(t1[i])
#Q3.
t1=10,30,5,2,40,12
l=t1[0]
for e in t1:
    if(e>l):
        l=e
print(l)
#Q4.
t1=10,30,5,2,40,12
l=t1[0]
for e in t1:
    if(e<l):
        l=e
print(l)
#Q5.
t1=10,30,5,2,40,12
l=0
sl=0
for e in t1:
    if(e>l):
        l=e
for e in t1:
    if(e>sl and e!=l):
        sl=e
print(sl)
#Q6.
t1=10,30,5,2,40,12
print(sorted(t1)) 
#Q7.
t1=10,30,5,2,40,12
t2=10,20,30,40,50,60
t1=sorted(t1)+sorted(t2)
print(t1)
print(sorted(t1))
#Q8.
t1=10,30,5,2,40,12
i=0
for e in t1:
    i=i+e
print(i)
#Q9.
t1=10,20,30,40,50,70
t2=10,20,30,40,50,60
i=len(t1)
j=len(t2)
if(i==j):
    k=0
    while(k!=i):
        if(t1[k]!=t2[k]):
            print("Not contain same element")
            break
        k+=1
    if(k==i):
        print("Contain same element")
else:
    print("t1 and t2 not contain same Number of element")
"""
