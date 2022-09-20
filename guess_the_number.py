# 1. Guess the number game

# a. Use random function to generate a number between 1 and 10 unknown to user

# b. Ask user for a number between 1 – 10

# c. If the user input is the same with the number that the computer generate, then display a positive message, such as “Nice job! You guessed it!

# d. If the user input is not the same, then display a try again message, such as “Not quite right, but nice try though”

# e. Don’t forget to have a way for the user to exit the program. For example: enter “e” to exit

import random
str2 = ''

while (str2 != 'e'):

    num1 = random.randint(1,10)

    print (num1)
    str2 = input("Please enter a number between one and ten: ")

    num2 = int(str2)

    print (str2)
    print (type(str2))

    print (num2)
    print (type(num2))

    print (type(str2))

    if num1 == num2:
        print ("Nice job! You guessed it!")

    else:
        print ("Not quite right, but nice try though")



# print (num2)