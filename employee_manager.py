from employee import Employee
from permanent_employee import PermanentEmployee
from contract_employee import ContractEmployee

class EmployeeManagement:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self._employees.append(employee)

    def remove_employee(self, employee):
        if isinstance(employee, Employee):
            self._employees.remove(employee)

    def search_employee(self, email):
        for employee in self._employees:
            if employee.email == email:
                return employee.display()
                print()
        return None

    def display_all_employees(self):
        for employee in self._employees:
            employee.display()
            print()

management = EmployeeManagement()

# add employees
contract_employee1 = ContractEmployee(1,"Yugandhar","Yugi@gmail.com" ,50000,6,2000)
contract_employee2 = ContractEmployee(2,"Hari","Hari@gmail.com" ,60000,7,5000)
permanent_employee = PermanentEmployee(3,"Rama","Rama@gmail.com", 80000, 2,4000)


# #add an employee
management.add_employee(contract_employee1)
management.add_employee(contract_employee2)
management.add_employee(permanent_employee)


# #Search an employee
management.search_employee("Yugi@gmail.com")

# #remove an employee
management.remove_employee(contract_employee2)

# #display all employees again
management.display_all_employees()