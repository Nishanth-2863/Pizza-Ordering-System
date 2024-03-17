class Food:
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description=description
    def food_details(self):
        print(f"Name: {self.name}\nPrice:{self.price}\nDescription: {self.description}")

class Pizza(Food):
    def __init__(self,name,price,description,category):
        super().__init__(name,price,description)
        self.category=category

    def food_details(self):
        super().food_details()
        print(f"Category: {self.category}")




Margherita=Pizza('Margherita',200.0,'deliciously tangy single cheese topping','vegetarian')
Peppy_Paneer=Pizza('Peppy Panner',250.0 ,'Chunky paneer with crisp capsicum and spicy red pepper','vegetarian')
CheeseNCorn=Pizza('CheeseNCorn',200,'Tasty Cheese n Corn Pizza','vegetarian')
ChickenDelight=Pizza('ChickenGoldenDelight',290,'Mmm! Barbeque chicken with a topping of golden corn','Non-vegetarian')
Chicken_Dominator=Pizza('Chicken Dominator' ,255,'Treat your taste buds with Double Pepper Barbecue Chicken','Non-vegetarian')
Keema_Do_Pyaza=Pizza('KEEMA DO PYAZA',265,'Delicious minced chicken keema topped','Non-vegetarian')