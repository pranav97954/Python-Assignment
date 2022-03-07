
a=int(input("Enter a number"))
if (a>=0):
    print("Positive")
else:
    print("Non-Positive")
#Q2
if (a%5==0):
    print("Divisible by 5")
else:
    print("Not divisible by 5")
#Q3
if (a%2==0):
    print("Even")
else:
    print("Odd")
#Q4
b=int(input("Enter second number"))
if (a>=b):
    if (a==b):
        print(a)
    else:
        print(a)
else:
    print(b)
#Q5

x=input("Enter a character")
y=input("Enter second character")
if(ord(x)>ord(y)):
    print(y,x)
else:
    print(x,y)
#Q6
if (a>=100 and a<1000):
    print("Given number is 3digit number")
else:
    print("Given Number is not a 3digit number")
