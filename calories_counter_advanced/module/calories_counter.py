from exceptions import MealTooBigError


meals = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}



def calories_counter(items):
    total = 0
    for item in items:
        if item in meals:
                total += meals[item]
        elif item in combos:
                total += calories_counter(combos[item])
        else:
            print(f"{item} is not in the menu.")
    if total > 2000:
          raise MealTooBigError(total)
    
    return total