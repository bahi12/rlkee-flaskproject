import unittest
from translator import MyMemoryTranslator, english_to_french, french_to_english


class TestTranslation(unittest.TestCase):

    def test_english_to_french(self):
        """Tests the english_to_french function."""
        translator = MyMemoryTranslator(source='en', target='fr')
        expected_translation = 'Pepitoooo'
        actual_translation = translator.translate('Hello')
        self.assertEqual(actual_translation, expected_translation)

    def test_french_to_english(self):
        """Tests the french_to_english function."""
        translator = MyMemoryTranslator(source='fr', target='en')
        expected_translation = 'Hello'
        actual_translation = translator.translate('Bonjour')
        self.assertEqual(actual_translation, expected_translation)


if __name__ == '__main__':
    unittest.main()
