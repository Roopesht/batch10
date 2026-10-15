import unittest
from mathematical import abs_add

class Test_maths(unittest.TestCase):
    def test_abs_add_2n(self):
        result = abs_add(-4,-2)
        self.assertEqual(result, 6)
    def test_abs_add_pn(self):
        result = abs_add(-4,4)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

