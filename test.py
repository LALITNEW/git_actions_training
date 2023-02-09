import unittest
from hello import hellow

class Testhellow(unittest.TestCase):

    def test_sum(self):
        calculation = hellow()
        self.assertEqual(calculation, "hello world")

if __name__ == '__main__':
    unittest.main()