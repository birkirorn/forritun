n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 0
number1= 1
number2= 2
number3= 3
#Always the last 3 numbers + together
#so we make 4 variables
#make a for statement in some range so you can plus the numbers together and then print the sum
print (number1)
print (number2)
print (number3)
#Here is n in range 
for n in range(n-3):
    sum= number1 + number2 + number3
    number1 = number2
    number2= number3
    number3=sum
    print(sum) 
