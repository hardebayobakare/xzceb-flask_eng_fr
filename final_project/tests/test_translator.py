"""
Module to test Translator module
"""
import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        """
        Test English to French Translation function
        """
        self.assertEqual(english_to_french('Quality'), 'Qualite')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        """
        Test English to French Translation function
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Qualite'), 'Hello')

unittest.main()
