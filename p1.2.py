# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:02:02 2021

@author: sharw
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
#input 
s = input(" enter string:")
#for counting bob
n=0
#loop for searching bob in input string
for i in range(len(s) - 2): 
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        n= n + 1 

print('Number of times bob occurs is:' + str(n))