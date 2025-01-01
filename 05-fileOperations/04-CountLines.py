linecount=0
with open('demo.txt','r') as file:
    while(file.readline()):
        linecount+=1
print("line count: %d" %(linecount))