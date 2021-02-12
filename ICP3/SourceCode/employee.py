
# Create class Employee
class Employee:

    # Employee counter
    numOfEmployee = 0
    # Sum of salaries
    sumOfSalaries = 0

    # Employee class constructor
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.numOfEmployee = Employee.numOfEmployee + 1
        Employee.sumOfSalaries = Employee.sumOfSalaries + self.salary

    def calcAvgSalary():
        return Employee.sumOfSalaries/Employee.numOfEmployee


# Create class Fulltime Employee and inherit from Employee class
class FullTimeEmployee(Employee):

    # Fulltime employee class constructor
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)




emp1 = Employee("Ahmed", "Alanazi", 10000, "IT")
emp2 = Employee("Ali", "Ali", 19000, "IS")
emp3 = FullTimeEmployee("John", "Gungur", 18000, "CS")
emp4 = FullTimeEmployee("Raj", "Komar", 11000, "AI")

print("\nFirst Name: " + emp1.name + "\nLast Name: " + emp1.family
      + "\nSalary: $%d" % emp1.salary + "\nDepartment: " + emp1.department)

print("\nFirst Name: " + emp2.name + "\nLast Name: " + emp2.family
      + "\nSalary: $%d" % emp2.salary + "\nDepartment: " + emp2.department)

print("\nFirst Name: " + emp3.name + "\nLast Name: " + emp3.family
      + "\nSalary: $%d" % emp3.salary + "\nDepartment: " + emp3.department)

print("\nFirst Name: " + emp4.name + "\nLast Name: " + emp4.family
      + "\nSalary: $%d" % emp4.salary + "\nDepartment: " + emp4.department)

calc = emp1.__class__.calcAvgSalary()
print("\nAverage Salary: $%d\n" % (calc))