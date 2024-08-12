import unittest
from nlp_model.story_generator import generate_story, StoryGeneratorError

class TestStoryGenerator(unittest.TestCase):

    def setUp(self):
        # Set up any initial configuration or state
        self.prompt = "Once upon a time in a land far away"
        self.bad_prompt = ""

    def test_generate_story_valid_prompt(self):
        # Test story generation with a valid prompt
        story = generate_story(self.prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)
        self.assertIn("Once upon a time", story)

    def test_generate_story_empty_prompt(self):
        # Test story generation with an empty prompt
        with self.assertRaises(StoryGeneratorError):
            generate_story(self.bad_prompt)

    def test_generate_story_special_characters(self):
        # Test story generation with a prompt containing special characters
        special_prompt = "The hero's journey & the dragon's lair!"
        story = generate_story(special_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)

    def test_generate_story_numeric_prompt(self):
        # Test story generation with a numeric prompt
        numeric_prompt = "12345"
        story = generate_story(numeric_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)

    def test_generate_story_long_prompt(self):
        # Test story generation with an extremely long prompt
        long_prompt = "A" * 1000
        story = generate_story(long_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)

    def test_generate_story_edge_case(self):
        # Test edge cases such as single-word prompts
        edge_prompt = "Magic"
        story = generate_story(edge_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)

    def test_generate_story_language_variations(self):
        # Test story generation with prompts in different languages
        spanish_prompt = "Había una vez en un reino lejano"
        french_prompt = "Il était une fois dans un pays lointain"
        story_spanish = generate_story(spanish_prompt)
        story_french = generate_story(french_prompt)
        self.assertIsInstance(story_spanish, str)
        self.assertIsInstance(story_french, str)
        self.assertGreater(len(story_spanish), 50)
        self.assertGreater(len(story_french), 50)

    def test_generate_story_with_dialogue(self):
        # Test story generation with a prompt that includes dialogue
        dialogue_prompt = "The king said, 'We must defend our kingdom!'"
        story = generate_story(dialogue_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)
        self.assertIn("king said", story)

    def test_generate_story_complex_structure(self):
        # Test story generation with a complex prompt structure
        complex_prompt = "In the year 3000, amidst a dystopian world, a hero rises."
        story = generate_story(complex_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)
        self.assertIn("hero", story)

    def test_generate_story_api_integration(self):
        # Test integration with external API if the story generator uses one
        api_prompt = "In the digital realm, data is power."
        story = generate_story(api_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)
    
    def test_story_generator_performance(self):
        # Test the performance of the story generation
        import time
        start_time = time.time()
        generate_story(self.prompt)
        end_time = time.time()
        self.assertLess(end_time - start_time, 2)  # Ensure the story is generated within 2 seconds

    def test_generate_story_emotionally_driven(self):
        # Test story generation with an emotionally charged prompt
        emotional_prompt = "The heart-wrenching tale of lost love"
        story = generate_story(emotional_prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 50)
        self.assertIn("lost love", story)

    def tearDown(self):
        # Clean up any resources or states
        pass

if __name__ == '__main__':
    unittest.main()
