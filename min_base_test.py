import unittest
from min_base import MinBase

class MinBaseTest(unittest.TestCase, MinBase):
    """class for all the test cases of min_base module
    """
    def test_greater_than_two(self):
        self.assertEqual(MinBase.find_min_base(self,9),2)
    def test_less_than_two(self):
        self.assertEqual(MinBase.find_min_base(self,1),2)
    def test_equal_to_two(self):
        self.assertEqual(MinBase.find_min_base(self,2),3)
    def test_first_thousand_positive_integers(self):
        self.assertEqual(MinBase.get_min_base(self),0)
    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            MinBase.find_min_base(self,-1)


if __name__ == '__main__':
    unittest.main()
