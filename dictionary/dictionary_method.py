a={
    "name":"pninfosys rohit",
    "college":"rjit",
    #college:45544,
    2:[1,2,3,3,1,1,(2,4,5.5)],
    4:("ram" ,"mohit"),
    "education":{'ram':"mca"},
    "city":"gwalior",
      }
# print(a["college78"])  ye wali line error degi isse bachne ke liye get laga diya
print(a.get("college1"))
print(a.keys())
print(type(a.keys()))
print(list(a.keys()))
print(a.values())
print(a.items())

#update dictionary
#print(a)
updatedict={
    "branch":"IT",
    "phone":"54545874",
    "salary":40000,
    "name":"sumit"  #update
}
a.update(updatedict)
print(a)