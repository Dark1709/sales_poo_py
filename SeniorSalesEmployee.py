from SalesEmployee import SalesEmployee
 
class SeniorSalesEmployee(SalesEmployee):
    def __init__(self, bonus_percentage: float, *args, **kwargs):
       super().__init__(*args, **kwargs) 
       self.set_bonus_percentage(bonus_percentage)
        
    def __str__(self):
        return f"{super().__str__()}\nbonus_percentage: {self.__bonus_percentage}"
    
    def set_bonus_percentage(self, bonus_percentage):
        self.__bonus_percentage = bonus_percentage
        
    @property
    def get_bonus_percentage(self):
        return self.__bonus_percentage
    
    def calculate_salary(self):
        commission = (self.get_commission_rate + self.__bonus_percentage) * self.get_sales 
        
        return commission + self.get_salary
    
julia = SeniorSalesEmployee(0.2, 1000, 0.1, 2185, 2000,"julia", 28 )
print(julia)
print(julia.get_name)
print(julia.get_age)
print(julia.get_employee_id)
print(julia.get_salary)
print(julia.get_sales)
print(julia.get_commission_rate)
print(julia.get_bonus_percentage)
salary = julia.calculate_salary()
print(salary)


""" roberto = SeniorSalesEmployee(0.5, 5000, 0.1, 2183, 1500,"roberto", 28 )
print(roberto) """