# IMPLICIT INHERITANE

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
    
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# OVERRIDE EXPLICITLY
print(f"{'-' * 20}\nOVERRIDE EXPLICITLY")

class Parent(object):
    def override(self):
        print("PARENT override()")
    
class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# ALTER PARENT INSIDE OF CHILD
print(f"{'-' * 20}\nALTER PARENT INSIDE OF CHILD")

class Parent(object):
    def altered(self):
        print("PARENT altered()")
    
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTEE PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()