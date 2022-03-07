"""
#Q1.
l1=input("Enter string").split(' ')
i=-1
while(i>=(-len(l1))):
    print(l1[i],end=" ")
    i-=1
print()
#Q3
l3=[]
l1=input("Enter string").split(' ')
print(l1)
for e in l1:
    l2=[]
    for i in e:
        l2.append(i)
    i=-1
    while(i>=(-len(l2))):
        l3.append(l2[i])
        i-=1
    l3.append(" ")
print("".join(l3))
#Q2
a=input("Enter password")
c=0
for e in a:
    if(e.isdigit()==True):
        for e in a:
            if(e.isalpha()==True):
                c+=1
                print("it is aphanumeric")
                break
        break
if(c==0):
    print("Not a alphanumeric")
#Q4.
l1=input("Enter string").split(' ')      
print("".join(l1))
#Q5
a=input("Enter a string")
b=input("Enter anoter string to find")
print(a.count(b))      
#Q7
l2=[]
l1=input("Enter city name seperated by comma").split(',')
print(l1)
l2=sorted(l1)
print(l2)       
"""
#Q8
#Q6
