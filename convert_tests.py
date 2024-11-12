import unittest
from convert import str_to_float

class TestStrToFloat(unittest.TestCase):
    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14"), 3.14)
        self.assertEqual(str_to_float("0"), 0.0)
        self.assertEqual(str_to_float("-2.71"), -2.71)

    def test_invalid_float(self):
        self.assertIsNone(str_to_float("abc"))
        self.assertIsNone(str_to_float("3.14.15"))
        self.assertIsNone(str_to_float(""))

    def test_edge_cases(self):
        self.assertEqual(str_to_float("1e10"), 1e10)
        self.assertEqual(str_to_float("0.0"), 0.0)

if __name__ == '__main__':
    unittest.main()

