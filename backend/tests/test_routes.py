import unittest
from src.routes import app
from flask import json

class TestRoutes(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        # Test the health check route
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'OK')

    def test_story_route(self):
        # Test the story generation route
        response = self.app.post('/api/story/generate', 
                                 data=json.dumps({'prompt': 'A hero rises'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('story', data)

    def test_story_route_missing_prompt(self):
        # Test the story generation route with missing prompt
        response = self.app.post('/api/story/generate', 
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

    def test_poetry_route(self):
        # Test the poetry generation route
        response = self.app.post('/api/poetry/generate', 
                                 data=json.dumps({'prompt': 'A moonlit night'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('poetry', data)

    def test_poetry_route_missing_prompt(self):
        # Test the poetry generation route with missing prompt
        response = self.app.post('/api/poetry/generate', 
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

    def test_character_route(self):
        # Test the character generation route
        response = self.app.post('/api/character/generate', 
                                 data=json.dumps({'prompt': 'A mysterious wanderer'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('character', data)

    def test_character_route_missing_prompt(self):
        # Test the character generation route with missing prompt
        response = self.app.post('/api/character/generate', 
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

    def test_script_route(self):
        # Test the script generation route
        response = self.app.post('/api/script/generate', 
                                 data=json.dumps({'prompt': 'A space odyssey'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('script', data)

    def test_script_route_missing_prompt(self):
        # Test the script generation route with missing prompt
        response = self.app.post('/api/script/generate', 
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

    def test_routes_performance(self):
        # Test the performance of the route handlers
        import time
        start_time = time.time()
        self.app.post('/api/story/generate', 
                      data=json.dumps({'prompt': 'A hero rises'}),
                      content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, 2)  # Ensure the response is generated within 2 seconds

    def tearDown(self):
        # Clean up any resources or states
        pass

if __name__ == '__main__':
    unittest.main()
