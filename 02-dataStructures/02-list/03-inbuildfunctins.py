#append, extend, remove, pop, insert, sort

list1=[10,20,30,40,50]

print("list1 values are", list1)

list1.append(60)

print("Values appending into list1" ,list1)

list2=[70,80,90,100,110,120,99]
print(list2)

print("combine both list2 into list1")

list1.extend(list2)

print(list1)

print("remove 99 from list 1")

list1.remove(99)

print(list1)

print("remove last value in the list1")
list1.pop()
print(list1)

print("remove the list value at index 4")

list1.pop(4)
print(list1)

print("sort the list")

list1.sort()

print(list1)

print("sort the list in reverse order")
list1.sort(reverse=True)
print(list1)