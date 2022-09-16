import csv
from  pathlib import Path



class Item:
   FILE_NAME = Path("items.csv")
   discout= 0.8 # Class Atteribute
   fieldsnames = []
   all = [] 
   def __init__(self,name:str,price:float,quantity=0):
      # Some Validations 
      assert len(name) >2, "The length  Must be bigger than 2 characters "
      assert price >= 0 ,"The Price Must be Positive Numbers or Zero"
      assert quantity >=0 ,"The Quantity Must be Zero or above! "

      self.__name= name
      self.price = price
      self.quantity = quantity

      # Appening instances into all list
      Item.all.append(self)
   
   # Property Decorator => Read-Only Attribute 
   @property
   def name(self):
      print("Getting name attribute...")
      return self.__name
   @name.setter
   def set_name(self,value):
      print("setting name Attribute...")
      self.__name = value

   def calc_total_price(self):
      return self.price * self.quantity

   def apply_discount(self):
      self.price= self.price * self.discout
      return f"The price After Discount  {self.price}"


   @classmethod
   def create_new_item(cls):
      
      # Prompt User For Item Information 
      name= input("Enter Product Name: ")
      price = float(input("Enter The Price: "))
      quantity = int(input("Enter The quantity: "))
      fields_names = [name,price,quantity]
      # Loop thru lst and Append Items in Item.filedsnames lst 'class Atterbute' 
      for item in fields_names:
         Item.fieldsnames.append(item)
      # print(Item.fields_names)

      # Check if csv File exist or Not and Append the item in Csv File 
      if not Item.FILE_NAME.exists():
         with open(Item.FILE_NAME,'w') as csvfile:
            items= csv.writer(csvfile)
            items.writerow(Item.fieldsnames)
            if items:
               print("New File has been Created And New Item Added!")
            return None

      with open(Item.FILE_NAME,'a') as csvfile:
         items= csv.writer(csvfile)
         items.writerow(Item.fieldsnames)
         if items:
            print(f"New Item Added in Existed File:{Item.FILE_NAME}")

   @classmethod
   def get_instance_from_csv(cls):
      with open("items.csv","r") as f :
         reader = csv.DictReader(f)
         item_lst = list(reader)
      for item in item_lst:
         print(item)

   def __repr__(self):
      return f"Item: {self.__class__.__name__} {self.name} - ${self.price} - Qun. {self.quantity}  "


class Phone(Item):
   def __init__(self,name,price,color,quantity=0):
      super().__init__(name, price,quantity)
      self.color = color

   @classmethod
   def create_new_item(cls):
      color= input("Color Name")
      Item.fieldsnames.append(color)
      return super().create_new_item()
      print(Item.fieldsnames)

# Phone.create_new_item()
# Item.create_new_item()
item1 = Item("Iphone11",1200,1)
# print(item1.name)
re=item1.set_name = "ipad"
print()
# print(item1.name)


# print(Item.__dict__)
# print(item1.__dict__)
# Item.get_instance_from_csv()





