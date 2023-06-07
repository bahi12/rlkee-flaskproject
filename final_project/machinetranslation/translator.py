"""AI is creating summary for Translation between EN:FR

Returns:
    [Text]: [description]
"""
from deep_translator import MyMemoryTranslator


def english_to_french(text):
    """AI is creating summary for english_to_french

    Args:
        text ([type]): [description]

    Returns:
        [type]: [description]
    """
    # write the code here
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation


def french_to_english(text):
    """AI is creating summary for french_to_english

    Args:
        text ([type]): [description]

    Returns:
        [type]: [description]
    """
    # write the code here
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation


FR = 'Bonjour'
EN = 'Hello'

result_fr = english_to_french(EN)
result_en = french_to_english(FR)

print(result_fr)  # Output: 'Bonjour !'
print(result_en)  # Output: 'Hello!'
