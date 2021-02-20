# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:03:53 2021

@author: sharw
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
 occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
 then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example,
 if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
#input
s = input(" enter string:")
#to indicat it is new sub string  or previous one 
flag=0
# 2 empty strings to store sub strings 
s1=""
s2=""
for i in range(1,len(s)):
      if(s[i]>s[i-1]): # cheking alphabetical order
        if(flag==0):
            s1=s[i-1]+s[i]
            flag=1
        else:
            s1+=s[i]
      else:
        if(len(s1)>len(s2)): #comparing  current string to previous one and updating 
            s2=s1
            flag=0
            
print('Value= ', s2)