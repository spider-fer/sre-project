import unittest
from methods import Token, Restricted
import requests


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()
        
    def test_generate_token_admin(self):
        payload = {'username': 'admin', 'password':'secret'}
        response = requests.post('http://localhost:8000/login', data=payload)
        self.assertEqual(response.status_code, 200)

    def test_generate_token_noadmin(self):
        payload = {'username': 'noadmin', 'password':'noPow3r'}
        response = requests.post('http://localhost:8000/login', data=payload)
        self.assertEqual(response.status_code, 200)
    
    def test_generate_token_bob(self):
        payload = {'username': 'bob', 'password':'thisIsNotAPasswordBob'}
        response = requests.post('http://localhost:8000/login', data=payload)
        self.assertEqual(response.status_code, 200)

    def test_generate_token_error(self):
        payload = {'username': 'fer', 'password':'pass'}
        response = requests.post('http://localhost:8000/login', data=payload)
        self.assertEqual(response.status_code, 403)

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjc2MzI3NTYyfQ.gnOiGLU81Uouj4kZiyUH-IFlCWSysb7GoZxSawK0_Ek'))

    def test_access_data_check(self):
        payload = {'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cfCI6IkpXVCJ9.eyJ1cs2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjc2MzI3NTYyfQ.gnOiGLU81Uouj4kZiyUH-IFlCWSysb7GoZxSawK0_Ekdf'}
        url = 'http://localhost:8000/protected'
        response = requests.get(url, headers=payload)
        self.assertEqual(response.status_code, 200)
    
    def test_access_data_invalid(self):
        self.assertEqual('Invalid Token', self.validate.access_data('eyJhbGciOiJIdUzI1NiIsghInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjc2MzI3NTYyfQ.gnOiGLU81Uouj4kZiyUH-IFlCWSysb7GoZxSawK0_Ek'))

if __name__ == '__main__':
    unittest.main()
