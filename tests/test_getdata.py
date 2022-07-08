from src.getdata import get_stock
from datetime import datetime
import unittest
import os


class TestGetdata(unittest.TestCase):
    def test_errors(self):
        self.assertRaises(AttributeError, get_stock, 'USIM5.SA', 1)
        self.assertRaises(AttributeError, get_stock, ['USIM5.SA'], '1d')

    def test_return(self):
        self.assertTrue(type(get_stock('USIM5.SA', '1d')[0]) is dict)
        self.assertTrue(type(get_stock('USIM5.SA', '1d')[1]) is str)


if __name__ == '__main__':
    if not os.path.exists('tests/logs'):
        os.makedirs('tests/logs')
    log_file = f'tests/logs/get_stock_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
