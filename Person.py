class Person:
    def __init__(self, name: str, age: int):
        self.set_name(name)
        self.set_age(age)
        
    def __str__(self):
        return f"name: {self.__name}\nage: {self.__age}"
    
    def set_name(self, name):
        self.__name = name
        
    @property
    def get_name(self):
        return self.__name   
    
    def set_age(self, age):
        self.__age = age
        
    @property
    def get_age(self):
        return self.__age 
        
""" maria = Person("Maria", 24)
print(maria)
print(maria.get_name)
print(maria.get_age)
         """