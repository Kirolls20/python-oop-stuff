# OOP SNIPPETS  -- constructors and instantiation 

class MyClass:
   '''
   Constuctors are generally  usued instantiating an object (Instance).
   In Python the __init__() method is called the constructor and is always called when an object is created.
   Constractors Can Be Two Types:
      1-Parameterized Constructor
      2-Non-parameterized Constructor (Defualt)

   '''
   # The Sentax of Constructor Declaration 
   # Default instantiation
   def __init__(self):
      self.x = 'Hello Python From The Constructor'
   
   def show(self):
      return self.x

# Object Test of The Class 
obj1= MyClass()
print(obj1.show())

class MyClass2:
   # parameterized instantiation
   def __init__(self,fname,lname):
      self.firstname = fname
      self.lastname = lname
   
   def display_name(self):
      return f" Your name is {self.firstname} {self.lastname}"

obj2 = MyClass2('kirolls','sabri')
print(obj2.display_name())