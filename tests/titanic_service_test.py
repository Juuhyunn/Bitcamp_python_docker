import unittest

from titanic.model.service import Service


class ServiceTest(unittest.TestCase):
    mock = Service()

    def test_new_model(self):
        print(self.mock.new_model('train.csv'))

if __name__ == '__main__':
    unittest.main()