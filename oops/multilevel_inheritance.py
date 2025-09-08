class person:
    country="india"
    def takebreath(self):
        print("gwalior")
class Employee(person):
    company="honda"
    def getsalary(self):
        print("salary 10000")
    def takebreath(self):
        super().takebreath()
        print("pninfosys")
class programer(Employee):
    company="fiverr"
    def getsalary(self):
        print(f"no salary to programers")
    def takebreath(self):
        super().takebreath()
        print("i am an programer so i am luckily breathing++..")
p=programer()
p.takebreath()            
                
            