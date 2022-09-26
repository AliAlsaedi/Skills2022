from task5 import *
import unittest
class Test_Python_Module(unittest.TestCase):
    def test_factors_ok(self):
        '''should not be empty'''
        self.assertTrue([]!=factors(5))
    def test_factors_not_ok(self):
        '''should  be empty'''
        self.assertTrue([]==factors(2))
    def test_is_prime_True(self):
        '''should return  True'''
        self.assertTrue(True==is_prime(3))
    def test_is_prime_False(self):
        '''should return  False'''
        self.assertFalse(True==is_prime(8))
    def test_vowels_there(self):
        '''return list should not be empty'''
        self.assertTrue([]!=vowels("Hello World"))
    def test_vowels_not_there(self):
        ''' return list should  be empty'''
        self.assertTrue([]==vowels("mnjhkd"))
    def test_len(self):
        '''Should be True'''
        self.assertTrue(11==len("Hello World"))
if __name__=="__main__":
    unittest.main()