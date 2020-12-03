#Excercise_1_Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
l1=["hyundai","maruti","kia","jeep","MG"]
l2=["Creta","Ertiga","Seltos","compass","Hector"]
a=list(zip(l1,l2))
print("The zipped list is :",a)

#Excercise_2_First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
l3=list(range(1,9))
Top_10_clean_cities=["Indore","Surat","NaviMumbai","Ambikapur","Mysore","Vijayawada","Ahmedabad","NewDelhi"]
b=tuple(zip(l3,Top_10_clean_cities))
print("Top 10 cleanliest cities in India are :",end="")
print(b)

#Excercise_3_Using sorted() function, sort the list in ascending order
alpha=list(range(50,0,-1))
print("The list befire sorting is :",alpha)
alpha.sort()
print("The sorted list is :",alpha)

#Excercise_4_Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
l4=list(range(1,51))
even_num=list(filter((lambda x:x%2==0),l4))
print("The even numbers are :",even_num)
odd_num=list(filter((lambda x:x%2!=0),l4))
print("The odd numbers are :",odd_num)





