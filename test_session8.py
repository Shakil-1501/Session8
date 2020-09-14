import pytest , os , inspect , re , random,session8
from decimal import Decimal
import math
import random
README_CONTENT_CHECK_FOR = ['Session : 8']


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


def test_function_calling_sep_dict():
    c=session8.counter2(session8.add,session8.dicA)
    c(3,6)
    c(4,5)
    l=session8.counter2(session8.mul,session8.dicA)
    l(3,2)
    l(4,5)
    x=session8.counter2(session8.div,session8.dicA)
    x(12,2)
    x(10,5)
    c=session8.counter2(session8.add,session8.dicB)
    c(2,4)
    c(3,7)
    c(2,3)
    l=session8.counter2(session8.mul,session8.dicB)
    l(3,2)
    x=session8.counter2(session8.div,session8.dicB)
    x(12,2)
    x(10,5)
    assert session8.dicA == {'add': 2, 'div': 2, 'mul': 2} and session8.dicB == {'add': 3, 'div': 2, 'mul': 1}


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"


def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"

