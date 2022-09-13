class Celsius:
   
   def __init__(self,temperature=0):
      self.__temperature = temperature

   def get_temperature(self):
      return self.__temperature
   
   # @temperature.setter
   def set_temperature(self,temp):
      # self.get_temperature = temp
      if temp < -273.15:
         raise ValueError("Temperature below -273.15 is not possible.")
      self.__temperature = temp
      return temp

   def to_fahrenheit(self):
      f=(self.__temperature)  *1.8 +32 
      return f"Temperature in fahrenheit: {f}"

   def __repr__(self):
      return f"Temperature: {self.__temperature}"

# Test Object
tem = Celsius(37)



