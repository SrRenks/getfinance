from datetime import datetime
from src.getdata import get_stock
from src.to_csv import to_csv
import unittest
import os


# chama a função get_stock para ter os dados normais
data = get_stock('USIM5.SA', '1d')
# altera os dados recebidos da função acima para testar os AttributeError
test_data = data[0], 1
test_data2 = 1, data[1]


class TestTocsv(unittest.TestCase):
    def test_errors(self):
        self.assertRaises(AttributeError, to_csv, test_data)
        self.assertRaises(AttributeError, to_csv, test_data2)


if __name__ == '__main__':
    if not os.path.exists('tests/logs'):
        os.makedirs('tests/logs')
    log_file = f'tests/logs/to_csv_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
