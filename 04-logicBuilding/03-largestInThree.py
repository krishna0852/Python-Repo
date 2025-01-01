number1=int(input("Enter number 1"))
number2=int(input("Enter number 2"))
number3=int(input("Enter number 3"))

largestNumber=number1 

if (number2>number1):
    largestNumber=number2 
if (number3>largestNumber):
    largestNumber=number3

print("The largest number is: %d" %(largestNumber))