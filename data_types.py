# write a program that takes two numbers from the user.
# and then it adds those numbers and shows the result to the user

number_1 = input ("What is your first number?")
number_2 = input ("What is your second number?")

 
print(number_1)
print(type(number_1))
print(number_2)
print(type(number_2))

# if i add strings, i am not getting the proper result
# so, i have to convert the data type from string to integer
number_1_int = int(number_1)
number_2_int = int(number_2)

print(number_1_int)
print(type(number_1_int))
print(number_2_int)
print(type(number_2_int))


sum = number_1_int + number_2_int
print("the sum is ", sum)
print(type(sum))
