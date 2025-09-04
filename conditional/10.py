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
# name=input("enter you name")
# p=input("enter physics marks")
# c=input("enter chemistry marks")
# m=input("enter maths marks")
# marksheet='''Name:<|name|>
# Marksheet 
# -----------
# physics| <|p|>
# chemistry| <|c|>
# maths| <|m|>
# '''
# marksheet=marksheet.replace("<|name|",name)
# marksheet=marksheet.replace("<|p|",p)
# marksheet=marksheet.replace("<|c|",c)
# marksheet=marksheet.replace("<|m|",m)
# print(marksheet)
# print("Total  |", int(p) +int(c)+int(m))
name=input("enter your name")
contact=input("enter your phone no.")
address=input("address")
university=input("enter your university name")
degree=input("degree")
skill= input("skills")
project=input("project")
hobbies=input("hobbys")
resume='''RESUME
NAME=<|name|>
CONTACT=<|contact|>
ADDRESS=<|address|>
UNIVERSITY=<|university|>
DEGREE=<|degree|>
SKILLS=<|skill|>
PROJECT=<|project|>
HOBBIES=<|hobbies|>
'''
resume=resume.replace("<|name|>\n",name)
resume=resume.replace("<|contact|>",contact)
resume=resume.replace("<|address|>",address)
resume=resume.replace("<|university|>",university)
resume=resume.replace("<|degree|>",degree)
resume=resume.replace("<|skill|>",skill)
resume=resume.replace("<|project|>",project)
resume=resume.replace("<|hobbies|>", hobbies)
print(resume)
 