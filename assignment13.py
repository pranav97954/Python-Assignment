"""
#Q1
l1=[]
n=int(input("Enter Value of N"))
for i in range(n):
    l1.append(i)
print(l1)
#Q2.
l2=[]
m=int(input("Enter Value of M for odd "))
for j in range(m):
    if(j%2!=0):
        l2.append(j)
        j+=1
    else:
        j+=1
print(l2)
#Q3.
l3=[]
o=int(input("Enter Value of O for even "))
for k in range(o):
    if(k%2==0):
        l3.append(k)
        k+=1
    else:
        k+=1
print(l3)
#Q4
l4=[]
a=int(input("Enter value of natural number "))
for e in range(a):
    l4.append(e**2)
print(l4)
#Q5
l5=[int(s) for s in input("Enter list number").split(',')]
b=max(l5)
print(b)
#Q6
l5=[int(s) for s in input("Enter list number").split(',')]
b=min(l5)
print(b)
#Q7
sum=0
l5=[int(s) for s in input("Enter list number").split(',')]
for e in l5:
    sum=sum+e
print(sum)
#Q8
a=[10,20,30,"abcde","we",23]
print(a)
b=[]
for e in a:
    if(type(e)==int):
        b.append(e)
print(b)
#Q11.
a=[int(e) for e in input("Enter list").split(',')]
a.sort()
print(a)
#Q12.
a=[int(e) for e in input("Enter list").split(',')]
sum=0
n=len(a)
for e in a:
    sum=sum+e
average=sum/n
print(average)
#Q13.
l1=[]
l1=input("Enter city name").split(',')
print(l1)
#Q15.
l1=[]
l1=[int(s) for s in input("Enter all number").split(',')]
print(l1)
even=0
odd=0
for e in l1:
    if e%2==0:
        even=even+e
    else:
        odd=odd+e
print("Even ",even)
print("Odd",odd)
"""
