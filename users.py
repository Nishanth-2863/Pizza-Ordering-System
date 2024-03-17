import json
class User:
    def __init__(self):
        self.users=self.load_users()
    def load_users(self):
        try:
            with open("users.json","r") as file:
               self.users=json.load(file)
        except FileNotFoundError:
            self.users={}
        return self.users
    def save_users(self):
            with open("users.json","w") as file:
                json.dump(self.users,file)
    def register_user(self,name,email,password):
        if email in self.users:
            print(f'Already registered User...')
            return False
        else:
            self.users[email]={"name":name,"password":password}
            self.save_users()
            print(f'Registered Successfully....')
            return True
    def login_user(self,email,password):
        if email in self.users and password==self.users[email]['password']:
                print(f'Login Successfull....')
                print(f'Welcome {self.users[email]["name"]}')
                print()
                return True
        else:
            print(f'Invalid username or password')
            return False









