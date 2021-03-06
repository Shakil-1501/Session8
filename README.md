# Session : 8

## Objective

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
- Write a closure that gives you the next Fibonacci number - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a  global dictionary variable with the counts - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

&nbsp;
``` html 
    check,summation,counter,counter2,check_fibonacci
                            
                            
                          

```
&nbsp;
- Write a test file, that tests all of the functions mentioned above + the other basic ones 
- Test file must contain at least 1 tests for each function


---
&nbsp;
## Files
 - Test File : [PyTest file](https://github.com/Shakil-1501/Session8/blob/master/test_session8.py)
 - Code: [Method Implemantation](https://github.com/Shakil-1501/Session8/blob/master/session8.py)
 - colab File: [![a](https://github.com/jagatabhay/TSAI/blob/master/openincolablogo.JPG)](https://colab.research.google.com/drive/18aU2U-RO4w09l7RJYoCtJ0XVF5-xOjqv?usp=sharing)
&nbsp;
---
&nbsp;

## Functions
| Serial No  | Name | Functionality |
| ---------- | --------- | ------ |
| 1 | check |The function takesin function as parameters and returns True/False based on length of docstring is greater than 50 characters or not|  
| 2 | check_fibonacci| This function returns the next number from fibnocci |
| 3 | counter |The function takes in function as parameters and returns the global dictionary which gives the frequency of each function |
| 4 | counter2| The function takes in function as parameters and returns the separate dictionary which gives the frequency of each function for different user |


## Test Cases Results
| Serial No  | Test Case | Result |
| ---------- | --------- | ------ |
| 1 | README File Exists | Pass |
| 2 | RREADME Words Counts | Pass |
| 3 | README proper description | Pass |
| 4 | RREADME Formatting | Pass |
| 5 | Proper identation and  PEP8 guidelines | Pass |
| 6 | Function name not defined with capital letters | Pass |
| 7 | test_docstring_length | Pass |
| 8 | test_fibonacci | Pass |
| 9 | test_function_calling_single_dict | Pass |
| 10 | test_function_calling_sep_dict | Pass | 

---

## Authors INFO
   
   Email : md.shakiluzzaman@gmail.com
   
   -[![](https://github.com/jagatabhay/TSAI/blob/master/logo.png)](https://www.linkedin.com/in/md-shakiluzzaman-894707129/)
