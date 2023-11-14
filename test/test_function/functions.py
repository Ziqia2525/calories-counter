from .constants import calories, combos, meals2, combos2, meals_dict, combos_dict, meals_dict_id
from .constants import meals_price_dict, combos_price_dict, meals_price_dict_id

def calories_counter(*meals):
    total = 0
    for meal in meals:
        try:
          if isinstance(meal, list):
            for item in meal:
                total += calories[item]
          elif meal in combos:
            for item in combos[meal]:
                total += calories[item]
          else:
            total += calories[meal]
        except KeyError:
            total = None
            print('The item is not on the menu')
        
    return total



def com_calories_counter(*meals):
    total = 0
    for meal in meals:
        try:
          if isinstance(meal, list):
            for item in meal:
                total += meals_dict[item]
          elif meal in combos_dict:
            for item in combos_dict[meal]:
                total += meals_dict_id[item]
          else:
            total += meals_dict[meal]
        except KeyError:
            total = None
            print('The item is not on the menu')
        
    return total



def price_counter(*meals):
    total = 0
    for meal in meals:
        try:
          if isinstance(meal, list):
            for item in meal:
                total += meals_price_dict[item]
          elif meal in combos_price_dict:
                total += combos_price_dict[meal]
          else:
            total += meals_price_dict[meal]
        except KeyError:
            total = None
            print('The item is not on the menu')
        
    return total







