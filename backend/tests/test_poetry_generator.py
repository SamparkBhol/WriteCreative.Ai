import unittest
from nlp_model.poetry_generator import generate_poetry, PoetryGeneratorError

class TestPoetryGenerator(unittest.TestCase):

    def setUp(self):
        # Set up any initial configuration or state
        self.prompt = "In the silent night, under the moonlight"
        self.bad_prompt = ""

    def test_generate_poetry_valid_prompt(self):
        # Test poetry generation with a valid prompt
        poetry = generate_poetry(self.prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)
        self.assertIn("night", poetry)

    def test_generate_poetry_empty_prompt(self):
        # Test poetry generation with an empty prompt
        with self.assertRaises(PoetryGeneratorError):
            generate_poetry(self.bad_prompt)

    def test_generate_poetry_special_characters(self):
        # Test poetry generation with a prompt containing special characters
        special_prompt = "The stars & the moon, together they swoon!"
        poetry = generate_poetry(special_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)

    def test_generate_poetry_numeric_prompt(self):
        # Test poetry generation with a numeric prompt
        numeric_prompt = "7 days a week, 24 hours a day"
        poetry = generate_poetry(numeric_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)

    def test_generate_poetry_long_prompt(self):
        # Test poetry generation with an extremely long prompt
        long_prompt = "B" * 500
        poetry = generate_poetry(long_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)

    def test_generate_poetry_haiku_format(self):
        # Test poetry generation in a specific format like Haiku
        haiku_prompt = "An old silent pond"
        poetry = generate_poetry(haiku_prompt)
        self.assertIsInstance(poetry, str)
        self.assertEqual(len(poetry.splitlines()), 3)  # Haiku has 3 lines

    def test_generate_poetry_language_variations(self):
        # Test poetry generation with prompts in different languages
        spanish_prompt = "En la noche oscura"
        french_prompt = "Dans la nuit tranquille"
        poetry_spanish = generate_poetry(spanish_prompt)
        poetry_french = generate_poetry(french_prompt)
        self.assertIsInstance(poetry_spanish, str)
        self.assertIsInstance(poetry_french, str)
        self.assertGreater(len(poetry_spanish), 20)
        self.assertGreater(len(poetry_french), 20)

    def test_generate_poetry_with_rhyme(self):
        # Test poetry generation with a rhyme scheme
        rhyme_prompt = "The sun sets, the stars align"
        poetry = generate_poetry(rhyme_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)
        self.assertIn("align", poetry)

    def test_generate_poetry_complex_structure(self):
        # Test poetry generation with a complex prompt structure
        complex_prompt = "In the labyrinth of dreams, shadows dance"
        poetry = generate_poetry(complex_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)
        self.assertIn("shadows dance", poetry)

    def test_generate_poetry_api_integration(self):
        # Test integration with external API if the poetry generator uses one
        api_prompt = "In the digital forest, echoes of silence"
        poetry = generate_poetry(api_prompt)
        self.assertIsInstance(poetry, str)
        self.assertGreater(len(poetry), 20)

    def test_poetry_generator_performance(self):
        # Test the performance of the poetry generation
        import time
        start_time = time.time()
        generate_poetry(self.prompt)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1)  # Ensure the poetry is generated within 1 second

    def tearDown(self):
        # Clean up any resources or states
        pass

if __name__ == '__main__':
    unittest.main()
