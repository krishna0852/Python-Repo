number=int(input("Enter a number to check it's prime or not"))

primeCount=0

for i in range(1,number+1):
    if (number % i == 0):
        print(i)
        primeCount=primeCount+1


if (primeCount==2):
    print("The number %d is a prime number" %(number))
else: 
    print("The number %d is not a prime number" %(number))