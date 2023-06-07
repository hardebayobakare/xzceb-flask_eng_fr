"""
Module for Translators
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Function to translate englisg text to french
    """
    #write the code here
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Function to translate french text to english
    """
    #write the code here
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
