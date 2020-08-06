from app import app
import unittest
import json

class BookTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_successful_books_date_asc(self):
        # Given
        payload = json.dumps({
            "type": "date",
            "order": "asc"
        })

        # When
        response = self.app.get('/books', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(201, response.status_code)

    def test_successful_books_date_desc(self):
        # Given
        payload = json.dumps({
            "type": "date",
            "order": "desc"
        })

        # When
        response = self.app.get('/books', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(201, response.status_code)

    def test_fail_books_date_asc(self):
        # Given
        payload = json.dumps({
            "type": "dat",
            "order": "asc"
        })

        # When
        response = self.app.get('/books', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(400, response.status_code)

    def test_fail_url(self):
        # When
        response = self.app.get('/lol', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(404, response.status_code)

    def test_successful_books_date(self):
        # When
        response = self.app.get('/books')

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(201, response.status_code)

    def test_fail_books(self):
        # When
        response = self.app.get('/books', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(bytes, type(response.data))
        self.assertEqual(400, response.status_code)
