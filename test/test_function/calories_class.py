
from .functions import com_calories_counter
from .functions import price_counter
from datetime import datetime

class Order:
    counter = 0

    def __init__(self, items, date=None):
        if isinstance(items, str):
           items = [items]
        self.order_id = f"ORDER-{Order.counter + 1}"
        Order.counter += 1
        self.order_accepted = False
        self.order_refused_reason = None
        self.date = date if date else datetime.now()
        self.items = items

    @property
    def calories(self):
        total_calories = com_calories_counter(*self.items)
        if total_calories is None:
            self.order_accepted = False
            self.order_refused_reason = "No item is ordered"
        elif total_calories > 2000:
            self.order_accepted = False
            self.order_refused_reason = "Total calories exceed 2000"
        else:
            self.order_accepted = True
            print(f"Order is accepted, total calorie:{total_calories}")
        return total_calories

    @property
    def price(self):
        total_price = price_counter(*self.items)
        if total_price is None:
            self.order_accepted = False
            self.order_refused_reason = "No item is ordered"
        else:
            self.order_accepted = True
            print(f"Order is accepted, price:{total_price}")
        return total_price

    def check_order_acceptance(self):
        self.calories 
        self.price
        print(self.date)

