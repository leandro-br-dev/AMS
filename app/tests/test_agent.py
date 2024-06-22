import unittest
from app import create_app, db
from app.models.agent import Agent

class AgentTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_agent(self):
        response = self.client.post('/agents/', json={
            'agent_name': 'Test Agent',
            'description': 'This is a test agent',
            'input_format': {},
            'output_format': {}
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Agent created successfully', str(response.data))

if __name__ == '__main__':
    unittest.main()