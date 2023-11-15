class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f"Meal is too big! {calories} is too much!"
        super().__init__(self.message)

class InvalidItemId(Exception):
    def __init__(self,item_id):
        self.message = f"{item_id} is not in the menu."
        super().__init__(self.message)

    