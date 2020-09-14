from typing import List
import time
import sys
import weakref
import random
from math import tan, pi


def check(fn):
    '''
    returns True/False based on length of docstring is greater than 50 characters or not
    input: function is passed
    count=50
    '''
    def check_docstring_l(*args, **kwargs):
        if len(fn.__doc__) > count:
            #print("docstring length is greater")
            return True
        else:
            #print("doccstring length is smaller")
            return False
    return check_docstring_l


def summation(a,b):
    '''
    returns the summation of a and b
    input is the two number a and b and storing it in c 
        
    '''
    c=a+b
    return c


dic={}
def counter(fn):
    '''
    returns the global dictionary which gives the frequency of each function 
    input: function passed
    '''
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        global dic
       
        cnt += 1
        dic[fn.__name__]=cnt
        #print(dic)
        return dic
    return inner


def add(a, b):
    '''
    returns the addition of two numbers
    '''
    return a + b


def mul(a, b):
    '''
    returns the product of two numbers
    '''
    return a*b


def div(a,b):
    '''
    returns the division of two numbers
    '''
    return a/b


dicA={}
dicB={}
def counter2(fn,dic):
    '''
    returns the separate dictionary which gives the frequency of each function for different user
    input: function and dictionary passed
    '''
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        global dicA
        global dicB
       
        cnt += 1
        dic[fn.__name__]=cnt
        #print(dic)
        return dic
    return inner


def check_fibonacci():
    '''
    returns the next number from fibnocci 
    '''
    a=0
    b=1
    count=0
    def fibonacci():
        nonlocal a
        nonlocal b
        nonlocal count
        count=count+1
        if count==1:
            
            return 0
        elif count==2:
             
            return 1
        else:
            c=a+b
            a=b
            b=c
            return b
    return fibonacci