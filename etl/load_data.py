import pandas as pd

def load(path='data/wdbc.csv'):
    df = pd.read_csv(path)
    print("Loaded", df.shape)
    return df