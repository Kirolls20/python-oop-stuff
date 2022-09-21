class Operation:
   def __init__(self,val):
      self.val = val
   
   def __mul__(self,other):
      '''
      __mul__() method is called to implement the arithmetic mulitiplication operation * 
      For example to evaluate the expression obj1 * obj2, Python attempts to call obj1.__mul__(obj2). 
      '''
      return self.val * other.val

   def __floordiv__(self,other):
      ''' 
         __floordiv__() method is called to implement floor division operation // 
         For example to evaluate the experssion obj1 // obj2 , python attempts to call obj1.__floordiv__(obj2).
      '''
      return self.val // other.val 
   
   def __truediv__(self,other):
      '''  
      __truediv__() method is called to implement true division operation / 
         For example to evaluate the experssion obj1 / obj2 , python attempts to call obj1.__truediv__(obj2).
      '''
      return self.val / other.val

   def __mod__(self,other):
      '''
         __mod__() method is called to implement the modulo operation using % operator , that return by default the remainder of 
         division , to evaluate the experssion obj1 % obj2 , Python attempts to call obj1.__mod__(obj2).
      '''
      return self.val % other.val
   
x= Operation(12)
y= Operation(4)

print(x*y)
print(x//y)
print(x/y)
print(x%y)

# The Same when you do ...

print(x.__mul__(y))
print(x.__floordiv__(y))
print(x.__truediv__(y))
print(x.__mod__(y))






