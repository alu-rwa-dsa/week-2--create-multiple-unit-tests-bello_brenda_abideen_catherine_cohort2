
import unittest
from DSA_Wk2_Q9 import *

class test_question9(unittest.TestCase):
    def test1(self):
        list1 = [9, 5, 3, 2, 6]
        list2 = [9, 5, 2, 6]
        self.assertNotEqual(question9(list1, list2), 8)


    def test2(self):
        list1 = [9, 5, 3, 2, 6]
        list2 = [9, 5, 2, 6]
        self.assertIsNotNone(question9(list1, list2))


    def test3(self):
        list1 = [9, 5, 3, 2, 6]
        list2 = [9, 5, 2, 6]
        self.assertEqual(question9(list1, list2), 3)



if __name__ == "__main__":
    unittest.main()