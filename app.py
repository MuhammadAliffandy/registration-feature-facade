import os
from modules.modules  import User
from modules.modules  import Validation
from modules.modules  import Notification

class Registration_Facade():
    def __init__(self):
        self.user = User()
        self.validation = Validation()
        self.notification = Notification()
    
    def registration_system(self ,username , email , password):
        if not self.validation.email_validation(email):
            print('Email tidak Sesuai')
        elif not self.validation.password_validation(password):
            print('''Harus mengandung huruf kecil
Harus mengandung huruf besar
Harus mengandung angka
Harus mengandung karakter khusus
Panjang minimal 8 karakter ''')
        else:
            self.user.add(username, email , password)
            self.notification.notification_user_added(username)
run = 'n'
while(run != 'y'):
    os.system('cls')
    print('\n==== Registration System ====\n')

    username = input('\nUsername : ')
    email = input('Email : ')
    password = input('Password : ')

    print('\n==================================\n')

    Reg = Registration_Facade()

    Reg.registration_system(username,email,password)

    key = input('\nTekan y untuk lanjut n untuk tidak (y/n) : ')
    if(key == 'y'):
        run = 'n'
    else:
        run = 'y'