from Employee import Employee

class SalesEmployee(Employee):
    def __init__(self, sales: float, commission_rate: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_sales(sales)
        self.set_commission_rate(commission_rate)
        
    def __str__(self):
        return f"{super().__str__()}\nsales: {self.__sales}\ncommission_rate: {self.__commission_rate}"
    
    def set_sales(self, sales):
        self.__sales = sales
        
    @property
    def get_sales(self):
        return self.__sales
    
    def set_commission_rate(self, commission_rate):
        self.__commission_rate = commission_rate
        
    @property
    def get_commission_rate(self):
        return self.__commission_rate
    
    def calculate_salary(self):
        commission = self.__commission_rate * self.__sales
        
        return commission + self.get_salary
    
    
""" falcao = SalesEmployee(5000, 0.1, 2180, 1000,"Falcao", 36, )
print(falcao)
print(falcao.get_name)
print(falcao.get_age)
print(falcao.get_employee_id)
print(falcao.get_salary)
print(falcao.get_sales)
print(falcao.get_commission_rate)
print(falcao.calculate_salary()) """

        