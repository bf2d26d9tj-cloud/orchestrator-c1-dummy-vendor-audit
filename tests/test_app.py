import unittest
from app import quote, export_csv


class FictionalDeliveryTests(unittest.TestCase):
    def test_standard_fee(self):
        self.assertEqual(quote(2), 25)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            quote(0)

    def test_csv_delivery_requirement(self):
        # Intentionally fails: the fictional vendor claims this feature is done.
        self.assertEqual(export_csv([2]), 'quantity,total\n2,25\n')


if __name__ == '__main__':
    unittest.main()
