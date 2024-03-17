
from menu import Menu
from Fooditems import Peppy_Paneer, ChickenDelight, CheeseNCorn, Margherita,Chicken_Dominator,Keema_Do_Pyaza
from Bill_calculation import Bill_calculation
class Order:
    def __init__(self):
        self.selected_items=[]
    def pizza_crusts(self):
        while True:
            pizza_crust={'Hand_Tossed':150,'Pan':100,'Cheese_Burst':200,'Thin_crust':180}
            valid_choices=list(pizza_crust.keys())
            print(f'Available Crust Types:')
            for index,(crust,price) in enumerate(pizza_crust.items(),start=1):
                print(f"{index}.{crust} Rs.{price}")
            user_choice_crust=int(input("Enter Your Choice: "))
            if user_choice_crust in range(1,len(valid_choices)+1):
                selected_crust_name=valid_choices[user_choice_crust-1]
                selected_crust_price=pizza_crust[selected_crust_name]
                selected_crust_details={'name':selected_crust_name,'price':selected_crust_price}
                print(f"{selected_crust_name} you selected")
                break
            else:
                print(f"invalid choice.. please choose between 1 and {len(valid_choices)}")

        return selected_crust_details

    def pizza_sizes(self):
        while True:
            pizza_size={'small':150,'Medium':200,'Large':300}
            valid_choices=list(pizza_size.keys())
            print(f"Available Sizes: ")
            for index,(size,price) in enumerate(pizza_size.items(),start=1):
                print(f"{index}.{size} {price}")
            user_choice=int(input(f"Select Pizza Size: "))
            if user_choice in range(1,len(valid_choices)+1):
                selected_size_name=valid_choices[user_choice-1]
                selected_size_price=pizza_size[selected_size_name]
                selected_size_details={'name':selected_size_name ,'price':selected_size_price}
                print(f"You choosen {selected_size_name} ")
                break
            else:
                print(f"Invalid option choose option between 1 and {len(valid_choices)}")

        return selected_size_details

    def pizza_selection(self,menu_details):
        value=True
        while value:
            print(f"Enter your Choice:\n1.Veg Pizza\n2.Non-Veg Pizza")
            user_choice=int(input())
            if user_choice==1:
                pizza_category=menu_details.veg_menu
            else:
                pizza_category=menu_details.non_veg_menu
            self.dishes = {index + 1: item for index, item in enumerate(pizza_category)}
            for index,items in self.dishes.items():
                print(index,end=' ')
                items.food_details()
                print()
            pizza_select=int(input("Choose your pizza: "))
            if pizza_select in self.dishes:
                    selected_pizza=self.dishes[pizza_select]
                    print(f"{selected_pizza.name} selected")
                    quantity=int(input("Enter an Quantity: "))
                    selected_crust_details=self.pizza_crusts()
                    selected_size_details=self.pizza_sizes()
                    self.selected_items.append({'pizza':selected_pizza.name,'price':selected_pizza.price,'quantity':quantity,'crust':selected_crust_details,'size':selected_size_details})
                    print()
                    options=int(input(f"Do you want to continue:\n1.yes\n2.No"))
                    if options==1:
                        continue

                    elif options==2:
                        value=False
                        break

                    else:
                        print(f"Invalid option..")

                    print(f'k')
            else:
                    print(f"invalid selection")

    def summary(self):
        while True:
            if not  self.selected_items:
                print(f"No items selected")
            else:
                print(f'Selected Items:')
            for index,item in enumerate(self.selected_items,start=1):
                print(f'Item {index}')
                print(f"Pizza: {item['pizza']}")
                print(f"Quantity: {item['quantity']}")
                print(f"crust: {item['crust']['name']}")
                print(f"size: {item['size']['name']}")
            user_choice=int(input(f"Do you confirm your order:\n1.Yes\n2.remove items\n"))
            if user_choice==1:
                bill_cal=Bill_calculation(self.selected_items)
                total=bill_cal.total_bill()
                bill_cal.payment(total)
                print(f'Your order has been placed.....')
                print(f"Thank you Visit again")

                return  self.selected_items
            elif user_choice==2:
                delete=int(input("Enter an item number to remove: "))
                if delete in range(1,len(self.selected_items)+1):
                    del self.selected_items[delete-1]
                    print(f'Item removed')
                    break
                else:
                    print(f'invalid number....')
            else:
                print(f'invalid choice try again....')


menu_items = Menu()


menu_items.add_items(Peppy_Paneer)
menu_items.add_items(Margherita)
menu_items.add_items(CheeseNCorn)
menu_items.add_items(ChickenDelight)
menu_items.add_items(Chicken_Dominator)
menu_items.add_items(Keema_Do_Pyaza)

#orders=Order()

#orders.pizza_selection(menu_items)
#orders.summary()