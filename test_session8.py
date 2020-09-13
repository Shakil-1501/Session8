import pytest , os , inspect , re , random,session8
from decimal import Decimal
import math
import random


def test_docstring_length():
    a=session8.check(session8.summation)
    assert a(5,4)==True


def test_fibonacci():
    k=session8.check_fibonacci()
    k()
    k()
    k()
    j=k()
    assert j==2


def test_function_calling_single_dict():
    c=session8.counter(session8.add)
    c(3,4)
    c(5,2)
    c(6,8)
    c=session8.counter(session8.mul)
    c(3,4)
    c=session8.counter(session8.div)
    k=c(12,3)
    assert k == {'add': 3, 'div': 1, 'mul': 1}


