import unittest
from translator import english_to_french, french_to_english
from translate import Translator


class TranslationTestCase(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_english_to_french(self):
        self.assertEqual(self.translator.translate(
            'Hello', from_lang='EN', to_lang='FR'), 'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(self.translator.translate(
            'Bonjour', from_lang='FR', to_lang='EN'), 'Hello')


if __name__ == '__main__':
    unittest.main()
