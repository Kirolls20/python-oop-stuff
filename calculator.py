class Calculator:

   def add(self,a,b):
      return a+b

   def subtract(self,a,b):
      return a-b
   
   def multiply(self,a,b):
      return a*b
   
   def divsion(self,a,b):
      return a/b

obj= Calculator()

while True:
   print("Choose The operation number or name or symbol:")
   print("1-Add (+)      2-Subtract (-)       3-multiply (*)        4-divsion(/)      5-Exit(e) ")

   user_inp= input("Enter The option: ")
   if user_inp == 'add'  or user_inp == '1' or user_inp == '+' :
      num1 = int(input("First Number:"))
      num2 = int(input('Second Number: '))
      result = obj.add(num1,num2)
      print(result)
      while True:
         print("1-Add (+)      2-Subtract (-)       3-multiply (*)        4-divsion(/)      5-Exit(e) ")
         user_inp= input("Enter The option: ")
         if user_inp == 'add' or user_inp == '1' or user_inp == "+" :
            other = int(input(" Other Number: "))
            result = obj.add(result,other)
            print(result)
         elif  user_inp == 'Subtract' or  user_inp == '2' or user_inp == '-' :
            other = int(input("Number: "))
            result = obj.subtract(result, other)
            print(result)
         elif user_inp == 'multiply' or user_inp == '3' or user_inp == '*' :
            other = int(input("Other Number: "))
            result = obj.multiply(result,other )
            print(result)
         elif user_inp == 'divsion' or user_inp == '4' or user_inp == '/' :
            other = int(input("Other Number: "))
            result = obj.divsion(result,other)
            print(result)
         elif user_inp == 'exit' or user_inp == '5' or user_inp == 'e' :
            exit()
         else:
            print("Invalid Option ")


   elif user_inp == 'Subtract' or user_inp == '2' or user_inp == '-' :
      num1 = int(input('First Number: '))
      num2 = int(input("Second Number: "))
      result = obj.subtract(num1, num2)
      print(result)
      while True:
         print("1-Add(+)      2-Subtract(-)       3-multiply(*)        4-divsion(/)      5-Exit(e) ")
         user_inp = input("Enter The operation: ")
         if user_inp == '1' or user_inp == 'add' or user_inp == '+':
            other = int(input("Other Number: "))
            result = obj.add(result,other)
            print(result)
         elif user_inp == '2' or user_inp == 'subtract' or user_inp == '-':
            other = int(input("Other Number: "))
            result= obj.subtract(result, other)
            print(result)
         elif user_inp == '3' or user_inp == 'multiply' or user_inp == '*' :
            other = int(input('Other Number: '))
            result = obj.multiply(result, other)
            print(result)
         elif user_inp == '4' or user_inp == 'divsion' or user_inp == '/':
            other = int(input('Other Number: '))
            result = obj.divsion(result, other)
            print(result)
         elif user_inp == '5' or user_inp == 'exit' or user_inp == 'e':
            exit()
         else:
            print("Invalid Input")


   elif user_inp == 'multiply' or user_inp == '3':
      num1 = int(input('First Number: '))
      num2 = int(input("Second Number: "))
      result = obj.multiply(num1, num2)
      print(result)
      while True:
         print("1-Add(+)      2-Subtract(-)       3-multiply(*)        4-divsion(/)      5-Exit(e) ")
         user_inp = input("Enter The Operation: ")
         if user_inp == '1' or user_inp == 'add' or user_inp == '+':
            other = int(input('Other Number: '))
            result = obj.add(result,other)
            print(result)
         elif user_inp == '2' or user_inp == 'subtract' or  user_inp == '-':
            other = int(input("Other Number: "))
            result = obj.subtract(result, other)
            print(result)
         elif user_inp == '3' or user_inp == 'multiply' or user_inp == '*': 
            other = int(input("Other Number: "))
            result = obj.multiply(result, other)
            print(result)
         elif user_inp == '4' or user_inp == 'division' or user_inp == '/' :
            other = int(input("Other Number: "))
            result = obj.divsion(result, other)
            print(result)
         elif user_inp == '5' or user_inp == 'exit' or user_inp == 'e':
            exit()
         else:
            print("Invalid Input!")


   elif user_inp == 'divsion' or user_inp == '4':
      num1 = int(input('First Number: '))
      num2 = int(input("Second Number: "))
      result = obj.divsion(num1, num2)
      print(result)
      while True:
         print("1-Add (+)      2-Subtract (-)       3-multiply (*)        4-divsion(/)      5-Exit(e) ")
         user_inp = input("Enter The Operation: ")
         if user_inp == '1' or user_inp == 'add' or user_inp == '+':
            other = int(input('Other Number: '))
            result = obj.add(result,other)
            print(result)
         elif user_inp == '2' or user_inp == 'subtract' or  user_inp == '-':
            other = int(input("Other Number: "))
            result = obj.subtract(result, other)
            print(result)
         elif user_inp == '3' or user_inp == 'multiply' or user_inp == '*': 
            other = int(input("Other Number: "))
            result = obj.multiply(result, other)
            print(result)
         elif user_inp == '4' or user_inp == 'division' or user_inp == '/' :
            other = int(input("Other Number: "))
            result = obj.divsion(result, other)
            print(result)
         elif user_inp == '5' or user_inp == 'exit' or user_inp == 'e' :
            exit()
         else:
            print("Invalid Input!")
   elif user_inp == '5' or user_inp == 'exit'  or 'e':
      break
   else:
      print("Invalid Input")

