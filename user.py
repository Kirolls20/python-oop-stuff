import bcrypt 
from pathlib import Path
import csv
class User:
   FILE_NAME = Path('users.csv')
   DATA_FIELDS= ['username','email','password']
   # follow the link below for documentation on how to use csv 
   # https://docs.python.org/3/library/csv.html

   def __init__(self,username=None,email=None,password=None):
      self.username = username
      self.email = email
      self.password = password


   def create_user(self):
      assert len(self.password) > 3, "Password is too short "
      self.username= input("User Name : ")
      self.email = input("Enter A vaild Email: ")
      password = input('Enter Password: ').encode()
      sault= bcrypt.gensalt()
      self.password= bcrypt.hashpw(password, sault)
      #userfields = [self.username,self.email,self.password.decode]
      user_data = {
         'username': self.username,
         'email': self.email,
         'password':self.password.decode()
      }

      if not User.FILE_NAME.exists():
         with open(User.FILE_NAME,'w') as csvfile:
            # data = csv.writer(csvfile)
            data = csv.DictWriter(csvfile, fieldnames=User.DATA_FIELDS)
            data.writeheader()
            # data.writerow(userfields)
            data.writerow(user_data)
            print("User stored successfully!!")
      else:
            with open(User.FILE_NAME,'a') as csvfile:
               # data = csv.writer(csvfile)
               data = csv.DictWriter(csvfile, fieldnames=User.DATA_FIELDS)
               # data.writerow(userfields)
               data.writerow(user_data)
               print("User stored successfully!!")

   def login(self):
      username= input("Username: ")
      password = input("Password: ").encode('utf-8')
      try:
         with open(User.FILE_NAME,'r') as csvfile:
            data= csv.DictReader(csvfile)
            for item in data:
               if  item['username'] == username and  bcrypt.checkpw(password, item['password'].encode())  == True :
                  found = True
                  break
               else:
                  found = False
            if found:
               print('User Existed!!')
            else:
               print("User Not Found!")
      except Exception as e:
         print(f"Error {e}")

   def __repr__(self):
      return f"(class {self.__class__.__name__},{self.username}-{self.email} password:{self.password} ) "


user = User()
user.create_user()
user.login()
