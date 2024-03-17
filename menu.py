
class Menu:
    def __init__(self):
        self.veg_menu=[]
        self.non_veg_menu=[]
    def add_items(self,item):
        if  item not  in self.veg_menu or item not in self.non_veg_menu:
            if item.category=='vegetarian':
                self.veg_menu.append(item)
            elif item.category=='Non-vegetarian':
                self.non_veg_menu.append(item)
                #print(f"{item.name} has been successfully added to menu..")
            else:
                print(f" The item already in the menu")

    def display(self,category):
        if category=='vegetarian':
            for items in self.veg_menu:
                items.food_details()
        else:
            for items in self.non_veg_menu:
                items.food_details()


    def remove_items(self,item):
        if item in self.menu:
            self.menu.remove(item)
            print(f"{item.name} has been successfully removed from the Menu")
        else:
            print(f"The item not in the list")


#menu_items=Menu()
"""
menu_items.display('vegetarian')
menu_items.add_items(Peppy_Paneer)
menu_items.add_items(Margherita)
menu_items.add_items(CheeseNCorn)

menu_items.add_items(ChickenDelight)
menu_items.add_items(Chicken_Dominator)
menu_items.add_items(Keema_Do_Pyaza)
"""