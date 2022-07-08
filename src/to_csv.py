from datetime import datetime
import pandas as pd
import os


def to_csv(data):
    if type(data[1]) != str:
        raise AttributeError('"data[1]" (Stock name) must be a string')
    if type(data[0]) != dict:
        raise AttributeError('"data[0]" (Dataframe) must be a dict')
    stock = data[1]
    data = data[0]
    time = pd.DataFrame(data=data['timestamp'], columns=['time'])
    time = time['time'].apply(lambda row: datetime.utcfromtimestamp(row).strftime('%d-%m-%Y %H:%M:%S'))
    df = pd.DataFrame(data=data['indicators']['quote'][0], index=None)
    df.insert(loc=0, column='time', value=time)
    df.set_index('time', inplace=True)
    now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    if not os.path.exists('historical_data'):
        os.makedirs('historical_data')
    if not os.path.exists(f'historical_data/{stock}'):
        os.makedirs(f'historical_data/{stock}')
    df.to_csv(f'historical_data/{stock}/{stock}_{now}.csv')
