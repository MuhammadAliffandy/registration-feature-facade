import os
import json
import random
import re

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "user.json")

class User():

    def add(self,username,email,password):
        id = random.randint(1,10000)
        
        userJsonData = {
            "id" : id,
            "username": f"{username}",
            "email": f"{email}",
            "password": f"{password}"
        }
        try:
            with open(json_path, "r") as file:
                prevData = json.load(file)

            userData = [
                *prevData,
                userJsonData,
            ]

        except json.JSONDecodeError:
            userData = [
                userJsonData,
            ]

        with open(json_path, "w") as file:
            json.dump(userData,file)
            
            return userJsonData

class Validation():
    def email_validation(self,email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.match(email_regex, email):
            return True
        else:
            return False
        
    def password_validation(self,password):
        min_length = 8
        password_regex = (
            r'^(?=.*[a-z])'  
            r'(?=.*[A-Z])'    
            r'(?=.*\d)'       
            r'(?=.*[@$!%*?&#])' 
            r'[A-Za-z\d@$!%*?&]' 
            r'{8,}$' 
        )
        
        if len(password) < min_length:
            return False

        if re.match(password_regex, password):
            return True
        else:
            return False

class Notification():
    def notification_user_added(self,username):
        print(f"Selamat, Akun atas nama {username} berhasil dibuat !!")

