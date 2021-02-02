
import unittest
from DSA_Wk2_Q8 import *
a = [[2, 7, 9], [8, 3, 7, 2, 0]]

class test_question8(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(merged_list([[2, 7, 9], [8, 3, 7, 2, 0]]))

    def test2(self):
        self.assertIn(7, merged_list([[2, 7, 9], [8, 3, 7, 2, 0]]))

    def test3(self):
        self.assertFalse(len(merged_list([[2, 7, 9], [8, 3, 7, 2, 0]])) > len([0, 2, 3, 7, 8, 9]))




if __name__ == "__main__":
    unittest.main()

