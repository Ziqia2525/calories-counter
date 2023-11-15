from unittest import TestCase

from module.exceptions import MealTooBigError
from module.functions import calories_counter, price_counter

class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = calories_counter(["meal-1","meal-2","meal-3"])
        self.assertEqual(result,1750,f"Expected 1750, got{result}")
    
    def test_count_combo_calories(self):
        result = calories_counter(["combo-1","combo-2"])
        self.assertEqual(result,1770,f"Expected 1770, got{result}")

    def test_count_meals_and_combos_calories(self):
        result = calories_counter(["meal-1","combo-1"])
        self.assertEqual(result,1670,f"Expected 1670, got{result}")

    def test_raise_error_if_calories_are_too_big(self):
        with self.assertRaises(MealTooBigError) as e:
            calories_counter(["combo-1","combo-1"])
            self.assertEqual(
                e.exception.message,
                "Meal is Too Big! 2140 Calories is Too Much!",
                "Wrong error message."
            )



class PriceCounterTestCase(TestCase):
    def test_count_meals_prices(self):
        result = price_counter(["meal-1","meal-2","meal-3"])
        self.assertEqual(result,18,f"Expected 18, got{result}")
    
    def test_count_combo_prices(self):
        result = price_counter(["combo-1","combo-2"])
        self.assertEqual(result,21,f"Expected 21, got{result}")

    def test_count_meals_and_combos_prices(self):
        result = price_counter(["meal-1","combo-1"])
        self.assertEqual(result,16,f"Expected 16, got{result}")