"""
n=int(input("Enter value of n "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)
#Q2
n=int(input("Enter value of n "))
i=1
sum=0
while i<=n:
    sum=sum+(i*i)
    i+=1
print(sum)
#Q3
n=int(input("Enter value of n "))
i=1
sum=0
while i<=n:
    sum=sum+(i*i*i)
    i+=1 
print(sum)
#Q4
n=int(input("Enter value of n "))
i=1
sum=0
while i<=n:
    sum=sum+(2*i-1)
    i+=1
print(sum)
#Q5
n=int(input("Enter value of n "))
i=1
sum=0
while i<=n:
    sum=sum+(2*i)
    i+=1
print(sum)
#Q6
n=int(input("Enter value of n to find factorial"))
i=1
while i<=n:
    if (n%i==0):
        print(i,end=",")
    i+=1
#Q7
x=input("Enter a number to count digit init")
count=0
for e in x:
  count +=1
print(count)
#Q8
x=input("Enter a number to calculate sum of digit in it ")
sum=0
for a in x:
    sum=sum+int(a)
print(sum)
"""
#Q9
x=int(input("Enter a number to reverse it "))
 