#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random
# Body
def check_tries(a):
	if a < 5:
		return True

	else:
		return False

def range_checker(x):
	if x >= 1 and x <= 25:
		return True 
	else:
		return False

def win_signal(winning_number):
	#This function will be invoked when all the conditions are met and the number is guessed correctly. 
	print("\n")
	print("Congragulations you have successfully guessed the number and have won the game.")
	print("\n")
	print ("Thanks for Playing!!!")

################################################################################
def main():
	print("Welcome to the Number guessing game developed in Python by Ankeet")
	print("\n")
	print("*"*70)
	print("The computer has generated a random number, the Player 1 has to guess the number")
	print("\n")
	import random
	number = random.randint(1,26)
	user_tries = 0
	#New Trial counter. Limit of 5 is for the users to guess the number
	while user_tries < 5:
		
		print("Please enter the number for your attempt ", user_tries+1 )
		print("\n")
		try:
			guessed_number = int(input(""))
			print ("\n")
								
			range_check = range_checker(guessed_number)


			if range_check == False:
				print ("Please enter the number between 1 and 25 (both inclusive). This will count as an attempt")
				user_tries += 1
				continue

			else:
				print ("The number is in the correct range of 1-25. This will count as an attempt")
				user_tries = user_tries + 1
				if guessed_number > number:
					print ("\n")
					print("Too high, Please try again !!")
					continue

				elif guessed_number < number:
					print ("\n")
					print ("Too Low, Please try again !!")
					continue

				else:
					print ("\n")
					print ("This is the correct match !!")
					win_signal(guessed_number)
					break
			#Passing the variable to check the range of the guessed number by the user.
		except:
			print ("Please enter only numbers, integers only. This will count as a valid attempt. Better luck in the next attempt")
			print("\n")
			user_tries= user_tries +1
			continue
	if user_tries >5:
		print ("Thanks for playing the game. You were not able to guess the number and have exhausted the attempts")
		print ("\n")
		print ("*"*70)
		print ("/n")
		print ("The computer had guessed the number randmonly and the same is", number)
		z= input ("Press any key to continue")
		
        

if __name__ == '__main__':
    main()
