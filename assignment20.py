def f1(n):
    for i in range(0,n):
        print(i,end=" ")
    print()
def f2(n):
    for i in range(n,0,-1):
        print(i,end=" ")
    print()
def f3(n):
    for i in range(1,n+1):
        print(i**2,end=" ")
    print()
def f4(n):
    for i in range(0,n):
        if(i%2!=0):
           print(i,end=" ")
    print()  
def f5(n):
    for i in range(0,n):
        if(i%2==0):
           print(i,end=" ")
    print()
def f6(n):
    e=0
    for i in range(0,n):
        e=e+i
    print(e)
def f7(n):
    return ((22/7)*r**2)

n=int(input("Enter value of n"))
f1(n)
print("Q2")
f2(n)
print("Q3")
f3(n)
print("Q4")
f4(n)
print("Q5")
f5(n)
print("Q6")
f6(n)
print("Q7")
r=int(input("Enter radies-"))
a=f7(r)
print(a)
#Q8
def factorial(n):
    l1=[]
    for e in range(1,n):
        if(n%e==0):
            l1.append(e)
    return l1       
n=int(input("Enter number"))
a=factorial(n)
print(a)
#Q9
def si(p,r,t):
    return((p*r*t)/100)
a=int(input("Enter Amount"))
b=int(input("Enter Rate"))
c=int(input("Enter Time in year"))
a=si(a,b,c)
print(a)
#Q10.
def avg(*t):
    return(sum(t)/len(t))
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
a=avg(a,b,c)
print(a)