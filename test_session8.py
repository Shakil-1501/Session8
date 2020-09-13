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

