# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:59:34 2016

@author: Fikrat Talibli
"""

n=5
while n>0:
    print(n)
    n=n-1
print('----')
print(n)

while True:
    line=input("> ")
    if line=='done':
        break
    print(line)

friends=["Farid","Elin","Farik"]    

for i in friends:
    print(i)

print("---")

smallest_so_far=74

print("Before the largest sofar",smallest_so_far)

for the_num in [3,41,12,3,74,15]:
    if the_num<smallest_so_far:
        smallest_so_far=the_num
    print(smallest_so_far,"<=",the_num)

print("Result is ",smallest_so_far)

sum=0
count=0
for the_current_num in [3,41,12,3,74,15]:
    count+=1    
    sum+=the_current_num
    print(count,sum)
    
print("Sum is ",sum)
print("Count is ",count)
print("Average is ",int(sum/count))


smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
