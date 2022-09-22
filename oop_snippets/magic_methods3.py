class Weight:
   def __init__(self,weight):
      self.weight = weight

   def __lt__(self,other):
      ''' 
      __lt__() Stands for  Less Than, a special method that describes less than operator in python,this method should return 
      true or false after comparing  between two objects x < y python internally calls x.__lt__(y) 
      '''
      return self.weight < other.weight
   def __le__(self,other):
      ''' 
         __le__ Means Less than or equal, a special method that describes less than  or equal operator in python,this method 
         should return  true or false after comparing  between two objects x <= y python internally calls x.__le__(y). 
      '''
      return self.weight <= other.weight

   def __gt__(self,other):
      '''
      __gt__() Stands for  Greater Than, a special method that describes less than operator in python,this method should return 
      true or false after comparing  between two objects x > y python internally calls x.__gt__(y) 
      '''
      return self.weight  > other.weight

   def __ge__(self,other):
      ''' 
         __ge__ Means Greater than or equal, a special method that describes less than  or equal operator in python,this method 
         should return  true or false after comparing  between two objects x >= y python internally calls x.__ge__(y). 
      '''
      return self.weight >= other.weight
   
   def __eq__(self,other):
      '''
      __eq__() Equality operator, special method that describes == in python , should return true or false after comparing between
      two objects x == y, python internally calls x.__eq__(y).
      '''
      return self.weight == other.weight

   def __ne__(self,other):
      '''
      __ne__() Not Equal and do the oppsite of __eq__() method it compare unequality between two objects  x != y.
      '''
      return self.weight != other.weight



# Test Cases

x= Weight(60)
y= Weight(70)

print(x<y) # True 
print(x<=y) # True
print(x>y) # False
print(x>=y) # False
print(x == y) # False
print(x!= y) # True
# The same way  to do..
print(x.__lt__(y)) # True 
print(x.__le__(y)) # True
print(x.__gt__(y)) # False
print(x.__ge__(y)) # False
print(x.__eq__(y)) # False
print(x.__ne__(y)) # True




