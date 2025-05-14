class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        print(f"Employee object for {self.name} created.")
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        def _del_(self):
            print(f"Employee object for {self.name} deleted.")
def create_and_delete_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = input("Enter salary:")
    emp = Employee(name, emp_id, department, salary)
    del emp
create_and_delete_employee()