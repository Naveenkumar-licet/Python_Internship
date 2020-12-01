#Excercise_1_Create a lambda function that multiplies argument x with argument y
a=lambda x,y:x*y
print(a(2,2))

#Excercise_2_Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce
fibo = lambda n: reduce(lambda x,_: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
print(fibo(5))

#Excercise_3_Write a Python program that multiply each number of given list with a given num-ber
nums=list(range(0,5))
f=list(map(lambda n:n*2,nums))
print(f)

#Excercise_4_Write a Python program to find numbers divisible by 9 from a list of numbers
n=list(range(1,99))
k=list(filter(lambda h:h%9==0,n))
print(k)

#Excercise_5_Write a Python program to count the even numbers in a given list of integers
n1=list(range(0,100))
j=list(filter(lambda b:b%2==0,n1))
print(j)
