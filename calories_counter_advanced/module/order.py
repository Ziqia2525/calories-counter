from module.exceptions import MealTooBigError, InvalidItemId
from module.functions import calories_counter, price_counter
import datetime

class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = f"order - {Order.counter}"
        if date is None:
           date = datetime.date.today()
        else:
           self.date = datetime.datetime.strptime(date,"%d-%b-%Y")
        self.items = items
        self._calories = None
        self._price = None
        try:
            self.calories
        except (MealTooBigError,InvalidItemId) as e:
            self.order_accepted = False
            self.order_refused_reason = e.message
            self._calories = 0
            self._price = 0
        else:
            self.order_accepted = True
            self.order_refused_reason = None

        
    
    @property
    def calories(self):
        if self._calories is None:
            self._calories = calories_counter(self.items)
        return self._calories

    @property
    def price(self):
        if self._price is None:
            self._price = price_counter(self.items)
        return self._price
