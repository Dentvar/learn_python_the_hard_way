# part A

# class Parent(object):

#     def implicit(self):
#         print("PARENT implict()")

# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# part B

# class Parent(object):

#     def implicit(self):
#         print("PARENT implict()")

# class Child(Parent):
#     def implicit(self):
#         print("CHILD implict()")

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# part C

# class Parent(object):

#     def altered(self):
#         print("PARENT altered()")

# class Child(Parent):
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")

# class Test(Child):
#     def altered(self):
#         print("Test")
        
# dad = Parent()
# son = Child()
# marius = Test()

# super(Test, marius).altered()
# dad.altered()
# son.altered()

# part D

# class Parent(object):

#     def overwrite(self):
#         print("PARENT, overwrite()")
    
#     def implicit(self):
#         print("PARENT, implicit()")
    
#     def altered(self):
#         print("PARENT, altered()")

# class Child(Parent):

#     def overwrite(self):
#         print("CHILD, Overwrite()")
    
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")


# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.overwrite()
# son.overwrite()

# dad.altered()
# son.altered()

#Part E

class Other(object):

    def overwrite(self):
        print("OTHER Overwrite")
    
    def implicit(self):
        print("OTHER implicit")
    
    def altered(self):
        print("OTHER altered")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def overwrite(self):
        print("CHILD Overwrite")

    def altered(self):
        print("CHILD BEFORE OTHER altered")
        self.other.altered()
        print("CHILD AFTER OTHER altered")


son = Child()

son.implicit()
son.overwrite()
son.altered()