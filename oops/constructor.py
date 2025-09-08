class Employee:
    company="pninfosys"
    def __init__(self):
        print("vikas jain")
    def getdetails(self,name,salary):
        print(self.company)
        print(f"the name of the pninfosys is name :",{name})
        print(f"the name of the employee is salary:",{salary})
rohit=Employee()
rohit.getdetails("raj",1234)
