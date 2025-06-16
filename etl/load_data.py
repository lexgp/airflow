import pandas as pd

def load(path='data/wdbc-kaggle.csv'):
    df = pd.read_csv(path)
    print("Loaded", df.shape)
    return df