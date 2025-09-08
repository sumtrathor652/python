# # no argument and no return value
# def add():
#     a=int(input("enter 1st no:"))
#     b=int(input("enter 2nd no:"))
#     c=a+b
#     print("sum=",c) 
# add()    
# # with argument no return value
# def add(a,b):
#     c=a+b
#     print("addition =",c)
# add(3,5)
# no argument with return value
# def add():
#     a=int(input("enter 1st no"))
#     b=int(input("enter 2nd no:"))
#     c=a+b
#     return c
# d=add()
# print("addition =" ,d)

# with argument with return value
def add(a,b):
    c=a+b
    return c
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
x=add(a,b)
print("addition =",x)

