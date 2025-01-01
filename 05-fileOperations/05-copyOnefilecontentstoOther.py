with open("demo.txt",'r') as sourceFile:
    with open("sample.txt" ,'w') as destFile:
        destFile.write(sourceFile.read()) #use for loop to copy contents line by line if it's a big file
