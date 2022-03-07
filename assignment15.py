"""
#Q1.
a=input("Enter a string")
i=a.count(' ')
l=len(a)
print("No. of character is",(l-i))
#Q2.
a=input("Enter a string")
f=input("Enter your sting to check found or not")
c=f.upper() in a.upper()
if c==True:
    print("Found")
else:
    print("Not found")
#Q3.
a=input("Enter a string")
print(a[::-1])
#Q4.
a=input("Enter a string")
f=input("find element")
i=a.count(f)
print(i)
#Q5.
a=input("Enter a string")
v=a.lower()
p=v.count('a')
q=v.count('e')
r=v.count('i')
s=v.count('o')
t=v.count('u')
print(p+q+r+s+t)
#Q6.
a=input("Enter a string")
v=a.upper()
print(v)
#Q7.
a=input("Enter a string")
v=a.lower()
print(v)
"""
#Q9.
a=input("Enter a string")
c=0
if(a.startswith(' ')):
    c+=1
elif(a.endswith(' ')):
    c+=1
i=a.count(' ')
words=(i+1)-c
print("No. of words is ",words)
