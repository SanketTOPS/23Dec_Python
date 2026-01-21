# Single Inheritance Example
class Parent:
    def func1(self):
        print("This is function 1 from Parent class.")

class Child(Parent):
    def func2(self):
        print("This is function 2 from Child class.")

print("--- Single Inheritance ---")
ob = Child()
ob.func1()
ob.func2()

# Multilevel Inheritance Example
class Grandparent:
    def funcA(self):
        print("Function A from Grandparent")

class Parent2(Grandparent):
    def funcB(self):
        print("Function B from Parent2")

class Child2(Parent2):
    def funcC(self):
        print("Function C from Child2")

print("\n--- Multilevel Inheritance ---")
ob2 = Child2()
ob2.funcA()
ob2.funcB()
ob2.funcC()
