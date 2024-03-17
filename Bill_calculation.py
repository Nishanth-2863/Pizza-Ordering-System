
class Bill_calculation():
    def __init__(self,selected_items):
        self.selected_items=selected_items
    def total_bill(self):
        bill=0
        for item in self.selected_items:
            pizza_price=item['price']
            pizza_crust=item['crust']['price']
            pizza_size=item['size']['price']
            pizza_quantity=item['quantity']
            total_item_price=pizza_price+pizza_crust+pizza_size
            bill+=total_item_price*pizza_quantity
            print(f"Total Bill: {bill}")
            return bill

    def payment(self,total_bill):
        value=True
        while value:
            print(f"Choose an payment method:\n1.cash\n2.Card\n")
            user_choice=int(input())
            if user_choice==1:
                print(f"----Thank you-----")
                value=False
                break
            elif user_choice==2:
                card_name=input(f"Enter Card name: ")
                cvv=int(input("Enter CVV: "))
                if card_name  and cvv:
                        print(f"Payment Processing....")
                        print(f"Payment Succesfull...")
                        value=False
                        break
                else:
                    print(f"Please Enter the card details")


        else:
            print(f"invalid selection")




