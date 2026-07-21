class Employee:
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
        
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
    def showLanguge(self):
        print(f"the name is {self.name} and he is good with {self.language} language")
        
a = Employee()
b = Programmer()