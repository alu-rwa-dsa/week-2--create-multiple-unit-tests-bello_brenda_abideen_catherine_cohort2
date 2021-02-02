#Brenda

import unittest
from DSA_Wk2_Q10 import *

class test_question10(unittest.TestCase):
    def test1(self):
        self.assertListEqual(show_ocurrence(4), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

    def test2(self):
        self.assertNotEqual(show_ocurrence(4), [1, 2, 3, 4])

    def test3(self):
        self.assertIn(1, show_ocurrence(4))



if __name__ == "__main__":
    unittest.main()