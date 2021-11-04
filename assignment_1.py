# Ask the user for a number
# then print the multiplication table for that number from 1 to 10.
# Your program should keep on running until the user says "quit"
#  
# That is .. if the user incorrectly inputs a string instead of a number
# Your program should  report out that ERRORS.

# Please study the following sample runs carefully.


# sample run 1  (positive testing)
Enter your number (or 'quit' to stop the program):  5
Here is your multiplication table

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
...
.


5 * 10 = 50


# sample run 2  (positive testing)
Enter your number (or 'quit' to stop the program):  9
Here is your multiplication table

9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
...
.


9 * 10 = 90


# sample run 3  (negative testing)
Enter your number (or 'quit' to stop the program):  abc
Error: you didn't give a number. I am exiting program.

====================

# sample run 4  (negative testing)
Enter your number (or 'quit' to stop the program):  abc
Error: you didn't give a number. 
Please try again.
Enter your number (or 'quit' to stop the program): 3

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
...
.


3 * 10 = 30

===================================

# sample run 5 (positive testing)
Enter your number (or 'quit' to stop the program):  quit
Thank you for playing the game. Good by!
