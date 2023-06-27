from SalesEmployee import SalesEmployee

class SeniorSalesEmployee(SalesEmployee):
    def __init__(self, name: str, age: int, employee_id: int, salary: float, sales: float, commission_rate: float, bonus_percentage: float):
       super().__init__(name, age, employee_id, salary, sales, commission_rate) 
       self.set_bonus_percentage(bonus_percentage)
        
    def __str__(self):
        return f"{super().__str__()}\nbonus_percentage: {self.__bonus_percentage}"
    
    def set_bonus_percentage(self, bonus_percentage):
        self.__bonus_percentage = bonus_percentage
        
    @property
    def get_bonus_percentage(self):
        return self.__bonus_percentage
    
julia = SeniorSalesEmployee("Julia", 45, 2110, 10000, 15000, 0.2, 0.5 )
print(julia)
print(julia.get_name)
print(julia.get_age)
print(julia.get_employee_id)
print(julia.get_salary)
print(julia.get_sales)
print(julia.get_commission_rate)
print(julia.get_bonus_percentage)