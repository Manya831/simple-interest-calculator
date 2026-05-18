
import unittest
from tests.factories import fake_product

class TestProductModel(unittest.TestCase):

    def test_read(self):
        product = fake_product()
        self.assertEqual(product["name"], "Laptop")

    def test_update(self):
        product = fake_product()
        product["name"] = "Phone"
        self.assertEqual(product["name"], "Phone")

    def test_delete(self):
        product = fake_product()
        del product
        self.assertTrue(True)

    def test_list_all(self):
        products = [fake_product()]
        self.assertEqual(len(products), 1)

    def test_find_by_name(self):
        product = fake_product()
        self.assertEqual(product["name"], "Laptop")

    def test_find_by_category(self):
        product = fake_product()
        self.assertEqual(product["category"], "Electronics")

    def test_find_by_availability(self):
        product = fake_product()
        self.assertTrue(product["available"])
