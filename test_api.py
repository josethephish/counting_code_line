import unittest
from api.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_count_lines(self):
        response = self.app.post('/count_lines', json={
            'code': "def foo():\n    pass\n# comment\n'''block comment'''"
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['lines_of_code'], 2)

    def test_count_lines_invalid_json(self):
        response = self.app.post('/count_lines', data="Not JSON")
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], "Request must be JSON")

    def test_count_lines_missing_code(self):
        response = self.app.post('/count_lines', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], "JSON must contain 'code' key")

if __name__ == '__main__':
    unittest.main()
