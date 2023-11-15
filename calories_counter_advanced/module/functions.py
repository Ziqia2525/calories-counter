from module.data import meals,combos
from module.exceptions import MealTooBigError,InvalidItemId

combos = {combo["id"]:combo for combo in combos}
meals = {meal["id"]:meal for meal in meals}

def calories_counter(items):
    total = 0
    for item in items:
        if item in meals.keys():
                total += meals[item]["calories"]
        elif item in combos.keys():
                total += calories_counter(combos[item]["meals"])
        else:
            raise InvalidItemId(item)
    if total > 2000:
          raise MealTooBigError(total)
    
    return total


def price_counter(items):
    total = 0
    for item in items:
        if item in meals.keys():
                total += meals[item]["price"]
        elif item in combos.keys():
                total += combos[item]["price"]
        else:
            raise InvalidItemId(item)

    
    return total