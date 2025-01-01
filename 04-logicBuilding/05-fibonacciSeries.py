number=int(input("Enter number to generate fibonaaci series"))
firstNum=0
secondNum=1

print(firstNum, end=" ")
print(secondNum, end=" ")

for i in range(2,number+1):
    nextSeq=firstNum+secondNum
    print(nextSeq, end=" ")
    firstNum=secondNum 
    secondNum=nextSeq
    


