name="  Palla Krishna Teja"

#find the length of the string

print("Name=%s and length is" %(name), len(name))

print("Removing spaces before and after name using strip function")

print("name=%s and after removing spaces is " %(name),name.strip())

strval="@@@####mayush"

#remove special characters @# in strval

print(strval)
print("removing special charaters",strval.lstrip("@#"))


strval2="somevalues@##$$"
print(strval2)
print("removing special characters right side", strval2.rstrip("@#%$"))