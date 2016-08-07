#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math

# Body
def welcome_message():
	print ("Hello Good Morning !! Welcome to the evaluator loop developed by Ankeet MIMS 2018")
	print ("/n")

def eval_loop():
	expression_user = 0.0
	welcome_message()
	counter = 0

	while expression_user != "done":
		expression_user = input ("Please enter the expression to be evaluated in the eval function")
		
		if expression_user == "done" and counter == 0:
			print ("Thanks for using the eval operator loop. The eval operator was not used a single time")
			break
		if expression_user == "done" and counter != 0:
			print ("Thanks for using the eval operator loop. The last expression being evaluated by the operator is", z )
			break
		print (eval (expression_user))
		z = (eval (expression_user))
		print ("\n")
		counter = counter + 1
		continue
		
	print ("End of Program")

###############################################################################
def main():
	eval_loop()
    #pass  # Remove this line and uncomment below once eval_loop is defined.
    
if __name__ == '__main__':
    main()
