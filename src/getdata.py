import requests


def get_stock(stock, range):
    if type(stock) != str:
        raise AttributeError('stock must be a string')
    if type(range) != str:
        raise AttributeError('range must be a string')
    interval_ranges = {
        '1d': '2m',
        '5d': '15m',
        '1mo': '30m',
        '6mo': '1d',
        'ytd': '1d',
        '1y': '1d'}
    if range in interval_ranges.keys():
        interval = interval_ranges[range]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{stock}?&interval={interval}&range={range}', headers=headers).json()
        return response['chart']['result'][0], stock
    else:
        raise ValueError('Invalid range, valid ranges: 1d, 5d, 1mo, 6mo, ytd and 1y.')
