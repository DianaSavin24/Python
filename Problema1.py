#C1: importul fisierului employee.py
from employee import Employee

#C2: mostenirea si modificarea clasei si metodelor             
class Manager(Employee):
    mrg_count=0
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)   
        self.departament=f"F36 {departament}"
        Manager.mrg_count+=1
        
    def display_employee(self):
        print("Departament: ", self.departament)
        

#C3: definirea obiectelor
p1=Manager("A", 20, "PR")
p2=Manager("B", 21, "HR")
p3=Manager("C", 31, "FR")
p4=Employee("D", 50)

#C4: apelarea metodei display_employee
p1.display_employee()
p2.display_employee()
p3.display_employee()
p4.display_employee()

#C5: afisarea valorii count-erelor
print("Numarul de salariati este: ", Employee.empCount)
print("Numarul de manageri este: ", Manager.mrg_count)
