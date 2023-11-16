from unittest import TestCase
from module.order import Order

class OrderTestCase(TestCase):
    def test_order_id_is_unique(self):
        initial_counter = Order.counter
        order_1 = Order([])
        self.assertEqual(order_1.order_id,f"order - {initial_counter + 1}")
        order_1 = Order([])
        self.assertEqual(order_1.order_id,f"order - {initial_counter + 2}")
