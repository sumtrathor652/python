# creating a empty se
a=set()
#adding values to an empty set
a.add(4) # only one element can add not  
a.add(5)
a.add(8)
a.add("pn")
a.add(5)
#a.add([5,7,8]) #not add list
a.add((4,5,6))
# a.add({5:7}) # not add dictionary
print(len(a))
a.remove(5)
print(a)
a.clear()
print(a)

