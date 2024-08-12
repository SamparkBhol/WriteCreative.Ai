import unittest
from nlp_model.character_generator import generate_character, CharacterGeneratorError

class TestCharacterGenerator(unittest.TestCase):

    def setUp(self):
        # Set up any initial configuration or state
        self.prompt = "A brave knight with a mysterious past"
        self.bad_prompt = ""

    def test_generate_character_valid_prompt(self):
        # Test character generation with a valid prompt
        character = generate_character(self.prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('name', character)
        self.assertIn('background', character)
        self.assertIn('traits', character)

    def test_generate_character_empty_prompt(self):
        # Test character generation with an empty prompt
        with self.assertRaises(CharacterGeneratorError):
            generate_character(self.bad_prompt)

    def test_generate_character_special_characters(self):
        # Test character generation with a prompt containing special characters
        special_prompt = "A wizard with powers beyond comprehension & a dark secret!"
        character = generate_character(special_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('name', character)
        self.assertIn('background', character)

    def test_generate_character_numeric_prompt(self):
        # Test character generation with a numeric prompt
        numeric_prompt = "The 7th son of the 7th son"
        character = generate_character(numeric_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('name', character)
        self.assertIn('background', character)

    def test_generate_character_long_prompt(self):
        # Test character generation with an extremely long prompt
        long_prompt = "C" * 500
        character = generate_character(long_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('name', character)
        self.assertIn('background', character)

    def test_generate_character_with_flaws(self):
        # Test character generation with a prompt that includes character flaws
        flaw_prompt = "A hero with a tragic flaw, such as hubris"
        character = generate_character(flaw_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('flaws', character['traits'])

    def test_generate_character_language_variations(self):
        # Test character generation with prompts in different languages
        spanish_prompt = "Un guerrero valiente con un pasado misterioso"
        french_prompt = "Un chevalier courageux avec un passé mystérieux"
        character_spanish = generate_character(spanish_prompt)
        character_french = generate_character(french_prompt)
        self.assertIsInstance(character_spanish, dict)
        self.assertIsInstance(character_french, dict)
        self.assertIn('name', character_spanish)
        self.assertIn('name', character_french)

    def test_generate_character_with_profession(self):
        # Test character generation with a specified profession
        profession_prompt = "A blacksmith turned hero"
        character = generate_character(profession_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('profession', character)

    def test_generate_character_complex_structure(self):
        # Test character generation with a complex prompt structure
        complex_prompt = "A warrior-monk, torn between his vows and his desire for revenge"
        character = generate_character(complex_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('conflict', character['background'])

    def test_generate_character_api_integration(self):
        # Test integration with external API if the character generator uses one
        api_prompt = "A cybernetic soldier in a dystopian future"
        character = generate_character(api_prompt)
        self.assertIsInstance(character, dict)
        self.assertIn('name', character)

    def test_character_generator_performance(self):
        # Test the performance of the character generation
        import time
        start_time = time.time()
        generate_character(self.prompt)
        end_time = time.time()
        self.assertLess(end_time - start_time, 2)  # Ensure the character is generated within 2 seconds

    def tearDown(self):
        # Clean up any resources or states
        pass

if __name__ == '__main__':
    unittest.main()
