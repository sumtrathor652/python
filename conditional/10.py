# letter='''Dear <|name|>,
# you are selected!
# have a great day ahead
# Thank you regards,
# pninfosys <|Date|>
# '''
# name= input("enter you name \n ")
# date=input("enter date \n")
# letter =letter.replace("<|name|>",name)
# letter=letter.replace("<|Date|>",date)
# print(letter)

name=input("enter you name")
p=input("enter physics marks")
c=input("enter chemistry marks")
m=input("enter maths marks")
marksheet='''Name:<|name|>
Marksheet 
-----------
physics| <|p|>
chemistry| <|c|>
maths| <|m|>

'''
marksheet=marksheet.replace("<|name|",name)
marksheet=marksheet.replace("<|p|",p)
marksheet=marksheet.replace("<|c|",c)
marksheet=marksheet.replace("<|m|",m)
print(marksheet)
print("Total  |", int(p) +int(c)+int(m))
