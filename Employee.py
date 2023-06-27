from Person import Person 

class Employee(Person):
    def __init__(self, employee_id: int, salary: float, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.set_employee_id(employee_id)
        self.set_salary(salary)
        
    def __str__(self):
        return f"{super().__str__()}\nemployee_id: {self.__employee_id}\nsalary: {self.__salary}"  
            
            
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
        
    @property
    def get_employee_id(self):
        return self.__employee_id
        
    def set_salary(self, salary):
        self.__salary = salary
        
    @property
    def get_salary(self):
        return self.__salary
    
    def calculate_salary(self):
        return self.__salary
    
    
    

    
""" jose = Employee(2155, 200, "jose", 34)
print(jose)
print(jose.get_name)
print(jose.get_age)
print(jose.get_employee_id)
print(jose.get_salary)
print(jose.calculate_salary()) """

