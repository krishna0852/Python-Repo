leapYearOrNot=int(input("Enter a year to check if it's a leap year or not"))

if (leapYearOrNot % 4 ==0 and leapYearOrNot % 100 !=0  or leapYearOrNot % 400 ==0):
    print("Give year %d is a leap year" %(leapYearOrNot))
else: 
    print("Given year %d is not a leap year" %(leapYearOrNot))