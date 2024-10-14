# Write a Python function that takes a string as input and counts the frequency of each character 
# in the string. The function should return the character frequencies in a dictionary 
# where keys should be the characters of input string and values represent the number of occurences of each characters.

# In this exercise, the function `character_frequency_counter` takes a string as input, 
# counts the frequency of each character, and then returns the character frequencies. 
# You can run the function with any string you'd like to test.

# Requirements:
# - Returns number of umber of occurences of each characters in a dictionary like in the following sample:
#     {'a': 1, 'b': 2, 'c':3}
# - In case of None input returns None
# - In case of Empty input string, returns None
# - Space characters are missing from output


def get_frequency(input_string:str) -> dict:
    if input_string is None or len(input_string) == 0:
        return None

    character_frequency_counter = {}
    for i in input_string:
        if i != ' ':
            if i in character_frequency_counter:
                character_frequency_counter[i] += 1
            else:
                character_frequency_counter[i] = 1
    return character_frequency_counter


# TEST OF CHARACTER FREQUENCY COUNTER EXCERCISE

import unittest
from excercise_2_character_frequency_counter import get_frequency

# AUTOMATED TEST, DO NOT MODIFY
class TestStringMethods(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(get_frequency("Géza kék az ég"), {'G': 1, 'é': 3, 'z': 2, 'a': 2, 'k': 2, 'g': 1})
        self.assertEqual(get_frequency("De a bikini felsőt már lazán dobja hátra A vitorláson amin elmegy Afrikába"), {'D': 1, 'e': 4, 'a': 6, 'b': 3, 'i': 6, 'k': 2, 'n': 4, 'f': 2, 'l': 4, 's': 2, 'ő': 1, 't': 3, 'm': 3, 'á': 5, 'r': 4, 'z': 1, 'd': 1, 'o': 3, 'j': 1, 'h': 1, 'A': 2, 'v': 1, 'g': 1, 'y': 1})

    def test_basic_test_cases_with_none(self):
        self.assertEqual(get_frequency([]), None)
        self.assertEqual(get_frequency(None), None)


if __name__ == '__main__':
    unittest.main()
