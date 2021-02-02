
import unittest as ut
import Question1 
import Question2


class FirstTest(ut.TestCase):

    def test_simple_string(self):
        self.assertIn("a", Question2.frequency("Hello I am mamane19").keys())

    def test_complex_str(self):
        self.assertEqual(Question2.frequency("Hey, can we be friends")[','], 1)
   
    


class SecondTest(ut.TestCase):

    def test_triple_space(self):
        self.assertEqual(Question1.remove_white_espace("hi   there  what's   up"), "hi there what's up")

    def test_trim_space(self):
        self.assertEqual(Question1.remove_white_espace("  hi  there  what's  up"), "hi there what's up")
    
    def test_trim_space(self):
        self.assertEqual(Question1.remove_white_espace("hi  there  what's  up  "), "hi there what's up")
    
    def test_both_spaces(self):
        self.assertEqual(Question1.remove_white_espace("  hi there what's up  "), "hi there what's up")

if __name__ == "__main__":
    ut.main()

