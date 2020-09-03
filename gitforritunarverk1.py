
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

#Program checks if integer is a positive number, if the number is negative then program will stop at the max
#if the input is positive then the program will go back one step to compare integers
#program will run until input is negative, then it halts
max_int=0
while num_int >=0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
