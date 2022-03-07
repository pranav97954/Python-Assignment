"""
#Q1
def f1(n):
    if(n>0):
        f1(n-1)
        print(n,end=" ")
n=int(input("Enter a number"))
f1(n)
#Q2
def f2(n):
    if(n>0):
        print(n,end=" ")
        f2(n-1)      
n=int(input("Enter a number"))
f2(n)
#Q3
def f3(n):
    if(n>0):
        f3(n-1)
        if(n%2!=0):
           print(n,end=" ")     
n=int(input("Enter a number"))
f3(n)
#Q4
def f4(n):
    if(n>0):
        if(n%2!=0):
           print(n,end=" ")     
        f4(n-1)
n=int(input("Enter a number"))
f4(n)
#Q5
def f5(n):
    if(n>0):
        f5(n-1)
        if(n%2==0):
           print(n,end=" ")     
n=int(input("Enter a number"))
f5(n)
#Q6
def f6(n):
    if(n>0):
        if(n%2==0):
           print(n,end=" ")     
        f6(n-1)
n=int(input("Enter a number"))
f6(n)
#Q7
def f7(n):
  if(n<=1):
        return n
  return n+f7(n-1)   
n=int(input("Enter a number"))
sum=f7(n)
print(sum)
"""
#Q10
def f10(n):
    if(n<=1):
        return n
    return n*f10(n-1)
n=int(input("Enter a number"))    
factorial=f10(n)
print(factorial)