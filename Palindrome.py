import unittest 
from Test_Pal import palindrome 
def palindrome(word): 
    return True 

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self): 
        result = palindrome("aba")
        self.assertEqual(result, True)

    def test_palindrome_simple_2(self):
        result = palindrome("neuquen")
        self.assertEqual(result, True)
    
    def test_palindrome_simple_3(self):
        result = palindrome("mendoza")
        self.assertEqual(result, False)

    def test_palindrome_simple_4(self):
        result = palindrome("nicolas")
        self.assertEqual(result, False)

    def test_palindrome_simple_5(self):
        result = palindrome("ala")
        self.assertEqual(result, True)

    def test_palindrome_simple_6(self):
        result = palindrome("rar")
        self.assertEqual(result, True)

    def test_palindrome_simple_7(self):
        result = palindrome("Agitafalsosusoslafatiga")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

