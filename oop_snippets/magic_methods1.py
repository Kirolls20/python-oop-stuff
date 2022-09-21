class Operation:
   # initilizing ob
   def __init__(self,num):
      self.num = num

   def __add__(self,other):
      ''' 
         The __add__(self,other) method in Python specifies what happens when you call + on two objects. 
         When you call obj1 + obj2, you are essentially calling obj1. __add__(obj2).
      
      '''
      return self.num + other.num
   
   def __sub__(self,other):
      '''
      __sub__(self, other) method returns a new object that represents the difference of two objects.
      It implements the subtraction operator - when you call obj1 - obj2 ou are essentially calling obj1. __sub__(obj2).
      '''
      return self.num - other.num

obj1= Operation(30)
obj2= Operation(20)

# __add__
print(obj1 + obj2)  # 10+ 20 = 30
print(obj1.__add__(obj2)) # 10 __add__ 20 = 30

#__sub__
print(obj1 - obj2)   
print(obj1.__sub__(obj2))
