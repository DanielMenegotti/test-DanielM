
# Name:           Action.py
# Author:         Daniel.M
# Created:        30/03/201
# Finished:       31/03/20
# ------------------------------------------------------------------------------
# importing the random functions
import random
# setting up a continuous program
while 1 > 0:
    # empty matrix
    matrix = []
    # Getting the users input
    user_input = input("Please type a number in for the dimension of the matrix or type quit to exit the program")
# allowing the if statement to check if the user wants to quit
    if user_input == "quit":
        break
    # found this try function? that seemed to work for testing if the user imputed letters
    # I'm pretty sure I did it some other way but I cannot remember how.
    try:
        int(user_input)
    except ValueError:
        print("Please do not enter any letter when imputing the dimension")
        continue



    # Creating the first of the three functions that creates a matrix depending on the entered dimension
    def create_matrix(dimension):
        # making sure the number imputed is ana actual positive number
        if dimension == str:
            return "Please type a number in with no letters included"
        if dimension < 1:
            return "An error has occurred please make sure the number input is a positive number and is greater than 1"
        # The final product of hours of testing things out, one single line for hours of trouble...
        # Creates random number in a matrix depending on the user imputed dimension, for example 2 would be [[?,?], [?,?]]
        # the problem with this is that the matrix will always be symmetrical so the second function does not really work
        new_matrix = [[random.randrange(0, 9) for i in range(dimension)] for j in range(dimension)]
        return new_matrix

    matrix = (create_matrix(int(user_input)))
    print(matrix)

    # The second function checks if the matrix is symmetrical
    def is_symmetric(my_list):
        # checks rows with the columns/lists? to test is symmetrical, [2,5],[6,8] will be symmetrical but [2,5],[8,9],[8,9] is not
        # I have no idea if this is what the assignments asks for but here is what I got.
        for row in my_list:
            if len(row) != len(my_list):
                return False
        return True
    print("Is the new matrix symmetrical?")
    print(is_symmetric(matrix))

    # final and last function transposes a matrix mixing the items up.
    # this I spent a good 4 hours on compared to the others taking 1 to 2 hours to make
    # I literally had to look up some examples to see how it worked, most people said to use zip(*my_list) which I tried
    # however that did not work then it was list(zip(my_list)) and so on so I just thought back to the programs I made before
    # I was reminded of an assignment (which i can't remember) back in java/Python? which I had to add things to a new list
    # and this is what I came up with after around half an hour of coding, so I really hope this is what was asked for.
    def transpose(my_list):
        new_list = []
        i = 0
        while i < len(my_list):
            j = 0
            transposed_list = []
            while j < len(my_list):
                transposed_list.append(my_list[j][i])
                j = j + 1
            new_list.append(transposed_list)
            i = i + 1
        return new_list

    print("Now let's transpose the matrix!")
    print(transpose(matrix))
    print("Thanks for using my matrix machine!")
    # I don't like matrices anymore... they make my head hurt.
