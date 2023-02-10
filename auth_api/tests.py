import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()
        
    #Commented this test since the token will always change
    # def test_generate_token(self):
    #    self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjc2MDU2NDI3fQ.lMe44mQKPbucFFI_onFfDErahtpCcbaVdoMpb3gahkw', self.convert.generate_token('admin', 'secret'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjc2MDU2MjQ1fQ.lBF79m4mjcqPI3f60xfotpm8hGLAvyRXZ5W_ptVFZKc'))

if __name__ == '__main__':
    unittest.main()
