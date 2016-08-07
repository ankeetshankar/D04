#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


# Body
def count(string, letter):
	word = string
	counter = 0
	for letter1 in word:
		if letter1 == letter:
			counter = counter +1

	print (counter)

###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    print("Hello World!")
    count("Ankeet","e")
    print("\n")
    count("MIMS","M")
    print("\n")
    count("USA","U")
    print("\n")
    print("End of Program")
    print("*" * 70)
    


if __name__ == '__main__':
    main()
