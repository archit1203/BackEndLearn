# class my_Class:
#     x=5

# p1 = my_Class()
# print(p1.x)

# class Person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age

# p1 = Person ('Archit' , 21)
# print(p1.name)

from ex3 import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)