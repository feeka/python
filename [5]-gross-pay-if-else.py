# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:30:05 2016

@author: Fikrat Talibli
"""

hrs = input("Enter Hours: ")
h = float(hrs)
rate=input("Enter Rate: ")
r=float(rate)

p=0

if(h>40):
	p=h*r+(h-40)*(10.5*0.5)
else:
    p=h*r
    
print(p)