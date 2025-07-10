import unittest
from app import create_app, db
from app.models import Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_add_student(self):
        res = self.client.post('/api/v1/student', json={
            "name": "Alice", "age": 20, "grade": "A"
        })
        self.assertEqual(res.status_code, 201)

    def test_get_students(self):
        self.client.post('/api/v1/student', json={
            "name": "Bob", "age": 22, "grade": "B"
        })
        res = self.client.get('/api/v1/student')
        self.assertEqual(res.status_code, 200)
        self.assertIn("Bob", str(res.data))

if __name__ == "__main__":
    unittest.main()

