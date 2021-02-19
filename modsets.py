import math

class PrintEvenNumber:
    #konstruktor obiektu
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        if (self.num % 2 == 0):
            return self.num
        else:
            return 0

class PrintOddNumber:
    #konstruktor obiektu
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        if (self.num % 2 != 0):
            return self.num
        else:
            return 0            

class Domain:
    def __init__(self):
        super()            

class Person(Domain):
    name = ""
    surname = ""
    age = 0
    def __init__(self, name, surname, age):        
        super().__init__()

        Person.name = name    
        Person.surname = surname           
        Person.age = age           

    @classmethod 
    def toString(self):
        return self.name + " " + self.surname  + " " + str(self.age)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi        

class Student(Person):
    index = ""
    def __init__(self, name, surname, age, index):        
        super().__init__(name, surname, age)
          
        Student.index = index        

    @classmethod 
    def toString(self):
        return  super().toString() + self.index 

class Employee(Person):
    profesion = ""
    def __init__(self, name, surname, age, profesion):        
        super().__init__(name, surname, age)
          
        Employee.profesion = profesion                

    @classmethod 
    def toString(self):
        pass
        return  super().toString() + self.profesion         