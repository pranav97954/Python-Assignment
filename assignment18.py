#Q1
s1={10,20,30,40,50,60}
print(len(s1))
#Q2
s2={20,30,50}
a=s2.issubset(s1)
if(a==True):
    print("issubset")
else:
    print("Not a subset")
#Q3
s3={70,90,110,45}
print("UNION",s1.union(s3))
#Q4
a=0
for e in s1:
    if(e>a):
        a=e
print(a)