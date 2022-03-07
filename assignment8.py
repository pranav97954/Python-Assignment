#Q1
a=int(input("Enter a number"))
if (a>=0):
    if(a==0):
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
#Q2
a=int(input("Enter the coefficeint of x^2"))
b=int(input("Enter the coefficient of x"))
c=int(input("Enter constant term"))
d=b*b-4*a*c
if(d>0):
    print("Real and distinct root")
elif(d==0):
    print("real and equal")
else:
    print("Imaginary")
#Q3
a=int(input("Enter a year"))
if (a%4==0):
    print("Leap year")
else:
    print("Not a leap year")
#Q4
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 3rd Number"))
if(a>=b and a>=c):
    print(a)
elif(b>=c):
    print(b)
else:
    print(c)
#Q5
a=int(input("Enter the value of month to know the how many day in that month"))
if(a==1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("31 Days")
elif(a==2):
    print("28 or 29 Days")
elif(a==4 or 6 or 9 or 11):
    print("30 Days")
else: 
    print("Enter a valid month in numeric format(1-12)")
#Q6
a=complex(input("Enter a complex number where i is replace by j "))
if(a.real>a.imag):
    print(a.real)
else:
    print(a.imag)
#Q7
m=int(input("Enter mark obtain in Maths"))
e=int(input("Enter mark obtain in English"))
h=int(input("Enter mark obtain in Hindi"))
s=int(input("Enter mark obtain in science"))
ss=int(input("Enter mark obtain in social science"))
if(m>=30 and e>=30 and h>=30 and s>=30 and ss>=30):
    mark=m+e+h+s+ss
    percentage=(mark/500)*100
    print(percentage)
    if(mark>=400):
        print("1st division")
    elif(mark>=300):
        print("2nd Division")
    elif(mark>=200):
        print("3rd Division")
    else: 
        print("Pass")
else:
    print("Fail")