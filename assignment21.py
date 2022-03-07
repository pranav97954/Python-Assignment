#Q1
def f1(n):
    return n%2
n=int(input("Enter a Number"))
a1=f1(n)
if(a1==0):
    print("Even")
else:
    print("Odd")
#Q2
def f2(n):
    return n%4
n=int(input("Enter a Number"))
a2=f2(n)
if(a2==0):
    print("Leap Year")
else:
    print("Not a Leap Year")
#Q3
def f3(n):
    l1=[]
    for e in n:   
        l1.append(e.upper())
    l=len(l1)
    print(l)
    if (l>0):
        i=0
        while i<=l//2:
            if(l1[i]==l1[l-1-i]):
                i+=1
            else: 
                print("Not a Palindrome")
                break
        if(i>l//2):
            print("Palindrome")
                            
n=input("Enter a string")
f3(n)
#Q4
def f4(n):
    count=0
    i=1
    while (i<n-1):
        if(n%i==0):
            count+=1
            i+=1
        else:i+=1    
    return count
n=int(input("Enter A Number -"))
i=f4(n)
if(i>1):
    print(n," is Not a Prime Number")
else:
    print(n," is a Prime Number")
#Q5
def f5(n):
    f1=5*n*n+4
    f2=5*n*n-4
    i=1
    while i<=f1//2 or i<=f2//2:
        if(i*i==f1 or i*i==f2):
            print(n,"is in Fibonacci series")
            break
        i+=1
    if(i*i != f1 and i*i != f2):
            print(n,"is not in Fibonacci series")
n=int(input("Enter a Number-"))
f5(n)
#Q6
def f6(n):
    count=0
    i=1
    while (i<n-1):
        if(n%i==0):
            count+=1
            i+=1
        else:i+=1    
    return count           
n1=int(input("Enter a Prime Number"))
n1+=1
while 1:
    i=f6(n1)
    if(i>1):
        n1+=1
        continue    
    else:
       print(n1)
       break
#Q7
def f7(n):
    f1=0
    f2=1
    while(f1<=n):
        print(f1)
        t=1
        if(f1>=2):
            t=f1
        f1=f1+f2
        f2=t
n=int(input("Enter a Number"))
f7(n)    
#Q8
def f8(n):
    a=10
    count=1

    while (n>=a):
        if(n%a):
            count+=1
            a=a*10
            continue
        
    print(count)   
n=int(input("Enter a Number-"))
f8(n)    
#Q9
def f9(word):
    count=0
    for e in word:
        count+=1
    print(count)
w=input("Enter a string-").split(' ')
f9(w)
#Q10
def f10(word):
    count=0
    for w in word:
        for e in w:
            e=e.upper()
            if(e=='A' or e=='E' or e=='I' or e=='O' or e=='U'):
                count+=1
    print(count)
w=input("Enter a string-").split(' ')
f10(w)