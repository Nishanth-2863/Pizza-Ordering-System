from users import User
from Order import Order, menu_items

def main():
    value=True
    while value:
        user_check=User()
        print(f'-----Fresh Pizza------')
        print(f'-----Welcome-----------')
        print(f'Enter your choice:\n1.Login\n2.Register\n')
        user_choice=int(input())
        if user_choice==1:
            email=input('Enter your email:').lower()
            password=input('Enter your password: ').lower()
            if user_check.login_user(email,password):
                order = Order()
                order.pizza_selection(menu_items)
                order.summary()
                value=False
                break
        elif user_choice==2:
            name=input('Enter an Name: ').lower()
            email=input('Enter a email: ').lower()
            password=input('Enter a password').lower()
            user_check.register_user(name,email,password)
    else:
        print(f'Invaild option')

if __name__=="__main__":
    main()

