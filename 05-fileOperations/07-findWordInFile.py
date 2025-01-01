wordToFind=input("Enter a string to check it's present in file or not")

found=False
with open('demo.txt','r') as file:
    for line in file:
        if wordToFind in line:
            print("Given word found: %s" %(line))
            found=True

if not found:
    print("%s word not found" %(wordToFind))
