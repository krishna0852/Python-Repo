name1="Krishna Teja"
name2="Palla"
name3="Krishna Teja"


#id -->it will print the memory address

print(id(name1))
print(id(name2))
print(id(name3))


#name1 and name3 has same address because both contains same value

#is, is not --> memory comparsion

print(name1 is name2) # it gives false because both has different values, so different adddresses
print(name1 is name3) #it gives true becase both are same

print(name1 is not name2)
print(name1 is not name3)


#in, not in --> data available for not

print("palla" in name1)
print("Teja" in name1)