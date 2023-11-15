from unittest import TestCase

from module.exceptions import MealTooBigError
from module.functions import calories_counter

class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = calories_counter(["meal-1","meal-2","meal-3"])
        self.assertEqual(result,1750,f"Expected 1750, got{result}")
    
    def test_count_combo_calories(self):
        result = calories_counter(["combo-1","combo-2"])
        self.assertEqual(result,1770,f"Expected 1770, got{result}")