#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """This program will only check if the first letter is a lower case character or not. Hence this function does not give us the correct output.  
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """
    #This function is wrong as the if statment has an error i.e. 'c'.islower() . 
    #The 'c' means that the string which has the value of 'c' is being checked will be used for the test giving the value True always.
    #The correct code could have been if c.islower():
        Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This code will return the flag status of the last character in the string s. eg. "Ankeet" as a string will give True as a result. 
    Only the last character status will be stored in flag and we are returning the value of the flag in the function. 
    Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    This function is incorrect as the False condition is or'd with the True or False condition. 
    This Or statement is in the loop and the last character will be Or'd and Flag will contain the result only for the last character not the entire string 
    Hence this function is incorrect.

    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    THis is the correct function. The putput of the function is also correct in the interpreter. 

    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print("Hello World!")


if __name__ == '__main__':
    main()
