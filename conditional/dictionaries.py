a={
    "name":"pninfosys rohit",
    "college":"rjit",
    #college:45544,
    2:[1,2,3,3,1,1,(2,4,5.5)],
    4:("ram" ,"mohit"),
    "education":{'ram':"mca"},
    "city":"gwalior",
}
print(a)
print(type(a))
print(a["name"])
print(a[2][6])
# print(a[0])  because in this they has no key
print(type(a[2][6]))
print(type (a[4]))
print(a["education"]["ram"])
print(a[2][6][1])
print(a["education"]["ram"][1])
print(a["city"][1])
print(type(a["city"]))
print(a["city"])
#change dictionary items
a[4]=(20,55,79,54)
a["name"]="raj"
print(a)
