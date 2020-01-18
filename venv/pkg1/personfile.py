#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         print(f"Person({self.name},{self.age} )")
#
#
# obj1= Person("Ronni", 20)
# obj1.__repr__()

a= []
b = a
c = []
print(id(a))
print(id(b))
print(id(c))
a+= [101]
print(a, b)
print(id(a))
print(id(b))
print(id(c))