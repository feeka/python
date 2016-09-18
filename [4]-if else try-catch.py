# -*- coding: utf-8 -*-


x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))

#line indenting plays great role in this case!
if x>y:
    print(str(x)+" is GREATER than "+str(y))
elif x<y:
    print(str(x)+" is LESS than "+str(y))
else:
    print(str(x)+" is EQUAL to "+str(y))

#try-catch
a=input("Enter number: ")
try: 
    g=int(a)
    print(g)    
except:
    print("Oops entered is not a number")
    
