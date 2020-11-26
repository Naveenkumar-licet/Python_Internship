# Excercise_1_Write a program to create a list of n integer values
n=int(input("Enter the number of values to be inside the list"))
L=list(range(0,n))
print(L)
# Add an item in to the list (using function)
L.append(5)
print("appended List is:",L)
#Delete (using function)
del L[5]
print("The List after deleted value",L)
#Store the largest number from the list to a variable
ma=max(L)
print("The maximum value in the list is ",ma)
#Store the Smallest number from the list to a variable
mi=min(L)
print("The minimum value in the list is ",mi)

#Excercise_2_Create a tuple and print the reverse of the created tuple
tup=(1,'two',3,'four',5)
tuprev=tup[::-1]
print("The original tupule is ",tup)
print("The reversed tupule is ",tuprev)

#Excercise_3_Create a tuple and convert tuple into list
tuplis=list(tup)
print("The list after converting from tupule is  ",tuplis)
