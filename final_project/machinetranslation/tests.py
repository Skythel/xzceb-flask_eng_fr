import unittest
import sys
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "Input cannot be null")
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(""), "Input cannot be null")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
unittest.main()