# 1. Create a simple class `Person` with name and age as attributes. 
# 2. Add a method to the `Person` class that prints a greeting. 
# class Person:
#     def __init__(self, name, age):
#         self.name =name
#         self.age=age

#     def greet(self):
#         print(f"Hii my name is {self.name} & i am {self.age} years old")

# myPerson = Person("SRP", 22)
# myPerson.greet()

# 3. Create a class with a class variable and instance variable. 
# class Superbike:
#     brand = "Kawasaki"  # Class variable

#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Brand: {Superbike.brand}, Model: {self.model}, Year: {self.year}")

# my_bike = Superbike("Z900", 2025)
# my_bike.display_info()

# 4. Create a private attribute in a class and access it using a method. 
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def get_account_info(self):
#         return f"Account Number: {self.__account_number}, Balance: {self.__balance}"
    
# my_account = BankAccount("387456297", 8300.0)
# print(my_account.get_account_info())

# 5. Create a class with a method that returns the square of a number.
# class MathOperations:
#     def square(self, num):
#         return num ** 2
# n=int(input("Enter a number to calculate its sqaure: "))
# my_math = MathOperations()
# print(f"The square of {n}: {my_math.square(n)}")

# 6. Create two objects of a class and demonstrate that they are independent.
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         return f"Car Brand: {self.brand}, Model: {self.model}"
    
#     def set_attributes(self, brand, model):
#         self.brand = brand
#         self.model = model
    
# car1 = Car("Buggati", "Chiron")
# car2 = Car("Honda", "Civic")
# print(car1.display_info())
# print(car2.display_info())

# 7. Create a class and use a method to set its attributes.
# car1.set_attributes("Tesla", "Model S")
# print(car1.display_info())

# 8. Demonstrate use of `isinstance()` with a class.
# def check_instance(obj, cls):
#     if isinstance(obj, cls):
#         return f"{obj.__class__.__name__} is an instance of {cls.__name__}"
#     else:
#         return f"{obj.__class__.__name__} is NOT an instance of {cls.__name__}"
# print(check_instance(car1, Car))

# 9. Demonstrate single inheritance in Python. 
# class Sports:
#     def __init__(self, name):
#         self.name = name
#     def play(self):
#         return f"Playing {self.name}"
# class Cricket(Sports):
#     def __init__(self, name, team_size):
#         super().__init__(name)
#         self.team_size = team_size

#     def play(self):
#         return f"Playing {self.name} with a team size of {self.team_size}"
    
#     def rules(self):
#         return "Cricket rules: 11 players per team, 6 balls per over, 50 overs in ODI."
    
# cricket = Cricket("Cricket", 11)
# print(cricket.play())

# # 10. Create a base class and derive two child classes with different methods(multi-level inheritance). 
# class Football(Sports):
#     def __init__(self, name, team_size):
#         super().__init__(name)
#         self.team_size = team_size

#     def play(self):
#         return f"Playing {self.name} with a team size of {self.team_size}"
    
#     def rules(self):
#         return "Football rules: 11 players per team, 90 minutes game time, no hands except for the goalkeeper."

# # 11. Demonstrate method overriding in inheritance.
# # 12. Use `super()` to call a parent class method.  
# class T20(Cricket):
#     def __init__(self, name, team_size, overs):
#         super().__init__(name, team_size)
#         self.overs = overs

#     def play(self):
#         return f"Playing {self.name} with a team size of {self.team_size} in {self.overs} overs format."
    
#     def rules(self):
#         print(super().rules())
#         return "T20 rules: 20 overs per side, maximum 2 fielders allowed for 6 overs of powerplay."

# # 13. Create an abstract base class using `abc` module. 
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# def make_sound(animal):
#     print(animal.sound())
# dog = Dog()
# cat = Cat()
# make_sound(dog)
# make_sound(cat)  

# # 14. Demonstrate multiple inheritance in Python.
# class T20:
#    def __init__(self, format, overs):
#        self.format = format
#        self.overs = overs
#    def play(self):
#        return f"Playing {self.format} with {self.overs} overs."
# class ODI:
#    def __init__(self, format, overs):
#        self.format = format
#        self.overs = overs
#    def play(self):
#        return f"Playing {self.format} with {self.overs} overs."
# class Cricket(T20, ODI):
#     def __init__(self, format, overs):
#         T20.__init__(self, format, overs)
#         ODI.__init__(self, format, overs)
#     def play(self):
#         return f"Playing {self.format} cricket with {self.overs} overs." 
# cricket = Cricket("T20", 20)
# print(cricket.play())
# cricket_od = Cricket("ODI", 50)
# print(cricket_od.play())


# 15.  Demonstrate encapsulation using getter and setter. 
# class Student:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age    # Private attribute
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive.")
# student = Student("SRP", 22)
# print(student.get_name())  # Output: SRP
# print(student.get_age())   # Output: 22
# student.set_name("Satya")
# print(student.get_name())  # Output: Satya
# student.set_age(25)
# student.set_age(-5)  # Output: Age must be positive.

# 16. Write a program to demonstrate polymorphism with a common method. 
# class Animal:
#     def sound(self): 
#         return "Some generic animal sound"
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# def make_sound(animal):
#     print(animal.sound())
# dog = Dog()
# cat = Cat()
# make_sound(dog)  # Output: Bark
# make_sound(cat)  # Output: Meow

# 17.  Create a class `Employee` with a method to display the number of employees created.
# class Employee:
#     employee_count=0
#     def __init__(self, name, positon):
#         self.name = name
#         self.position = positon
#         Employee.employee_count += 1

#     def display_employee_count(self):
#         return f"Total number of employees: {Employee.employee_count}"

# emp1=Employee("SRP", "Manager")
# emp2=Employee("Satya", "Developer")
# emp3=Employee("Juel", "Designer")
# print(emp3.display_employee_count())
    
# 18.  Demonstrate constructor overloading using default arguments.
# class Cricket:
#     def __init__(self, format="Test", max_overs=360):
#         self.format = format
#         self.max_overs = max_overs

#     def print_details(self):
#         return f"Cricket Format: {self.format}, Max Overs: {self.max_overs}"

# Cricket1 = Cricket()
# print(Cricket1.print_details())
# Cricket2 = Cricket("ODI", 100)
# print(Cricket2.print_details())
# Cricket3 = Cricket("T20", )
# print(Cricket3.print_details())

# 19.  Implement a bank account system with deposit and withdrawal methods. 
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amt):
#         if (amt > 0):
#             self.__balance += amt
#             print(f"Deposited: {amt}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdrawal(self, amt):
#         if 0 < amt <= self.__balance:
#             self.__balance -= amt
#             print(f"Withdrew: {amt}. New balance: {self.__balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def get_balance(self):
#         return self.__balance
    
# my_account = BankAccount("766754")
# my_account.deposit(1000)
# my_account.withdrawal(500)
# my_account.withdrawal(600)

# 20.  Create a class `Rectangle` with method to calculate area and perimeter. 
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         return self.length*self.breadth
    
#     def perimeter(self):
#         return 2*(self.length+self.breadth)

# print("Enter length & breadth of a rectangle to calculate its area & perimeter.")
# length = int(input("Enter length: "))
# breadth = int(input("Enter breadth: "))
# rect1=Rectangle(length, breadth)
# print(f"Area of rectangle: {rect1.area()} square units")
# print(f"Perimeter of rectangle: {rect1.perimeter()} units")

