"""
#Q1.
p=int(input("Enter a number"))
a=2
while a<p:
    if(p%a==0):
        print(p,"is not a prime number")
        break
    else:
        a+=1
if(a==p):
    print(p,"is prime number")
#Q2.
x=range(1,100)
for e in x:
    a=2
    while a<e:
        if(e%a==0):
            break
        else:
           a+=1
    if(a==e):
        print(e,end=" , ")
#Q3.
a=int(input("Enter first number"))
b=int(input("Enter second one"))
x=range(a,b)
for e in x:
    a=2
    while a<e:
        if(e%a==0):
            break
        else:
           a+=1
    if(a==e):
        print(e,end=" , ")
#Q5.
a=int(input("Enter a number"))
x=range(a)
for e in x:
    a=2
    while a<e:
        if(e%a==0):
            break
        else:
           a+=1
    if(a==e):
        print(e,end=" , ")
"""
#Q4.
"""
p=int(input("Enter a prime number to find another one"))
p+=1
a=2

    if(p%a==0):
        p+=1
    elif(p%a!=0 and p==a):
        print(p)
        break   
    else:
        a+=1
    
"""
#Q7.
a=1
b=1
while a<=25:
    print(a,end=" ")
    b=a 
    a=a+b