# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:58:27 2021

@author: sharw
"""
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
#input
s = input(" enter string:")
#for counting no. of vowel 
count = 0 

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print("Number of vowels: "+str(count))