#Q1.
a=int(input("Enter the value of N "))
l1=[]
for n in range(2,a):
    c=0
    i=2
    while i<n:
        if(n%i==0):
            c+=1
        i+=1
    if(c==0 and i==n):
        l1.append(n)
print(l1)
#Q2.
l1=[]
def sum(a,b):
    for i in range(3):
        c=[]
        for j in range(3):
            c.append((a[i][j]+b[i][j]))
        l1.append(c)
    print("Sum of given matrix is")
    for i in range(3):
        for j in range(3):
              print(l1[i][j],end=' ')
        print()             
    return 0
a=[]
for i in range(3):
    m=[]
    for j in range(3):
        m.append(int(input("Enter value")))
    a.append(m)
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')
    print()
b=[]
for i in range(3):
    m=[]
    for j in range(3):
        m.append(int(input("Enter value")))
    b.append(m)
for i in range(3):
    for j in range(3):
        print(b[i][j],end=' ')
    print()
sum(a,b)
#Q3.
l1=[]
def INPUT(d):
   for i in range(1,4):
        c=[]
        for j in range(1,4):
           c.append(int(input("Enter %d row value-"%i)))
        d.append(c)
   return d
def Product(a,b):
    for i in range(3):
        c=[]
        for j in range(3):
           c.append((a[i][j])*(b[i][j]))
        l1.append(c)
    return l1
def OUTPUT(e):
    for i in range(3):
        for j in range(3):
            print(e[i][j],end=" ")
        print()
    return 0
a=[]
b=[]
print("Enter Value of first matrix :-")
a=INPUT(a)
print("Enter Value of Second matrix :-")
b=INPUT(b)
print(" first matrix :-")
OUTPUT(a)
print("Second matrix :-")
OUTPUT(b)
Product(a,b)
print("Product of Two matrix is:-")
OUTPUT(l1)
#Q4.
l1=[int(s) for s in input("Enter value").split(',')]
l2=[int(s) for s in input("Enter value").split(',')]
l3=l1+l2
print(sorted(l3))
#Q5.
l1=['HELLO','PRANAV','HOW','ARE','YOU']
print(' '.join(l1))
