# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:20:44 2016

@author: Fikrat Talibli
"""

def hello(done):
    print(done)
    print('World')

#function
def greet(lang):
    word=''
    if lang=='es':
        word="Hola"
    elif lang=='fr':
        word="Bonjour"
    else:
        word="Hello"
        return word

big=max('123')

print(big)

print(greet("fr"))

hello("Hello")