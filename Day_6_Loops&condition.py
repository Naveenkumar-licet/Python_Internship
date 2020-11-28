#Excercise_1_program to loop through a list of numbers and add +2 to every value to elements in list
L=list(range(0,5))
print("Before adding",L)
for i in range(0,5):
    i=i+2
    print("after adding",i)

#Excercise_2_Write a program to get the below pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j,end="")
    print()

#Excercise_3_Python Program to Print the Fibonacci sequence
n=int(input("Enter the number of terms"))
n1=0
n2=1
count=0
print("The fibonacci series is")
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1

#Excercise_4_Explain Armstrong number and write a code with a function
def armstrong(nubmer):
    number=int(input("enter the number"))
    sum=0
    temp=number
    while temp > 0:
        nodig = temp % 10
        sum += nodig ** 3
        temp //= 10
        if(sum==number):
            print("Yess!!!!!Its an Armstrong number")
        else:
            print("The number you provided is not an Armstrong number")
armstrong(7)

#Excercise_4_Write a program to print the multiplication table of 9
tab=int(input("enter the number up to which table is to be calculated"))
print("Multiplication table for 9 is:")
for n in range(0,tab):
    mul=n*9
    print("9*",n,"=",mul)

#Excercise_5_Check if a integer is negative or positive
posneg=int(input("enter the number to find whether it is positive or negative"))
if(posneg>0):
    print("The number you have entered is positive")
else:
    print("The number yoy have entered is negative")

#Excercise_6_Write a program to convert the number of days to ages
days=int(input("enter the nunber of days you ave lived: "))
age=float(days/365)
print("You age is: ",age)

#Excercise_7_Trigonometry problem using math function write a program to solve using math function
import math
n=60
print("The sin value is: ",end="")
print(math.sin(n))
print("The cos value is: ",end="")
print(math.cos(n))
print("The tan value is: ",end="")
print(math.tan(n))

#Excercise_8_Create a calculator only on a code level by using if condition
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))
print("Choose the arithmetic function you want to do")
print("1.Addition")
print("2.Subrection")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice"))
if(ch==1):
    c=a+b
    print("The added value is: ",c)
elif(ch==2):
    c=a-b
    print("The subtracted value is: ",c)
elif(ch==3):
    c=a*b
    print("The multiplied value is: ",c)
elif(ch==4):
    c=a/b
    print("The divided value is: ",c)
else:
    print("Invalid choice")



