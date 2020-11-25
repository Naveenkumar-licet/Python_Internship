#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Excercise_1_Write a Python script to merge two Python dictionaries

car={"maruti":"alto","hyundai":"santro","kia":"seltos","jeep":"compass"}
bike={"hero":"splendor","bajaj":"platina","yamaha":"fz","ktm":"duke"}
vehicle=car.update(bike)
print(car)


# In[15]:


#Excercise_2_Write a Python program to remove a key from a dictionary
car={"maruti":"alto","hyundai":"santro","kia":"seltos","jeep":"compass"}
del car["hyundai"]
print(car)


# In[16]:


#Excercise_3_Write a Python program to map two lists into a dictionary
brand=["maruti","hyundai","kia","jeep"]
model=["alto","santro","seltos","compass"]
car=dict(zip(brand,model))
print(car)


# In[17]:


#Excercise_4_Write a Python program to find the length of a set
cities={"chennai","coimbatore","madurai","tirunelveli","trichy","thoothukudi"}
print(len(cities))


# In[18]:


set1={"bird","mammals","giraffe","camel","dog","cat","fish","crab","prawn"}
set2={"bird","mammals","human","coffee","tea","dosa","idly","vada pav"}
set1-=set2
print(set1)

