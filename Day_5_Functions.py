#Excercise_1_Create a function getting two integer inputs from user
import math
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
def arithmetic(a,b):
    c=a+b #Addition of two numbers
    print("The addition is ",c)
    d=a-b #Subtraction of two numbers
    print("The subracted value is ",d)
    e=a*b#Multiplication of two numbers
    print("The multiplied value is ",e)
    f=a/b#division of two numbers
    print("The divided value is ",f)
    return
arithmetic(a,b)

#Excercise_2_Create a function covid( )&it should accept patient name,and body temperature,
patient_name=input("Enter the patient's name")
Body_temperature=98
def covid(patient_name,Body_temperature):
    print("The Patient name is",patient_name +" and his body temperature is",Body_temperature)
    return
covid(patient_name,Body_temperature)