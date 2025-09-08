class papa:
    bike="007"
    def showdetails(self):
        print("this is an employee")
class son(papa):
    language="python"
    # bike="008"
    def getlanguage(self):
        print(f"the language is {self.language}")
    def showdetails(self):
        print("this is an programer")       
p=son()
p.showdetails()
print(p.bike)    