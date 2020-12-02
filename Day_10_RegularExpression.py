#Excercise_1_Write a Python program for all the cases which can check a string contains only a certain set of characters
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

#Excercise_2_Write a Python program that matches a word containing 'ab'
import re
def findab(text):
    patterns = '\w*ab.\w*'
    if re.search(patterns,text):
        return ('Found a match!')
    else:
        return ('Not matched!')
print(findab("abs"))

#Excercise_3_Write a Python program to check for a number at the end of a word/sentence
import re
def num(s):
    text = re.compile(r".*[0-9]$")
    if text.match(s):
        return ('Found int at end of string')
    else:
        return ('not found')
print(num("naveen4"))

#Excercise_4_
import re
results = re.finditer(r"([0-9]{1,3})","Exercises number 1, 3, 56, and 999 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

#Excercise_5_Write a Python program to match a string that contains only uppercase letters
import re
def match(text):
        patterns = '^[A-Z]*$'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return('Not matched!')

print(match("im doing internship at bestenlist"))




