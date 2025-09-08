class Employee:
    car="pninfosys"
    ecode=120
class freelancer:
    # car="google"
    level=0
    def upgradelvel(self):
        self.level=self.level+1
class programer(freelancer,Employee):
    # car="abcs"
    name="name"
p=programer()
print(p.car)
p.upgradelvel()