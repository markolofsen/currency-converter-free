import unittest
from currency_converter_free import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()

    def test_available_currencies(self):
        currencies = self.converter.available_currencies()
        self.assertIn("USD", currencies)
        self.assertIn("EUR", currencies)

    def test_convert_same_currency(self):
        result = self.converter.convert(100, "USD", "USD")
        self.assertEqual(result, 100)

    def test_convert_usd_to_eur(self):
        result = self.converter.convert(100, "USD", "EUR")
        self.assertIsNotNone(result)
        self.assertGreater(result, 0)

if __name__ == "__main__":
    unittest.main()
