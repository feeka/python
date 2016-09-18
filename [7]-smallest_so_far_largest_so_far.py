# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:24:49 2016

@author: Fikrat Talibli
"""

largest = 0
smallest = 7

while True:
    num=0    
    try:
        value=input("Enter a number: ")
        if(value=="done"):
            break
        num = int(value)
    except:
        print("Invalid input")
        continue
    if num < smallest : 
        smallest=num        
    if num > largest:
        largest=num
    

print("Minimum is ",smallest)
print("Maximum is ",largest)



