from data import meals,combos
from exceptions import MealTooBigError

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
            print(f"{item} is not in the menu.")
    if total > 2000:
          raise MealTooBigError(total)
    
    return total