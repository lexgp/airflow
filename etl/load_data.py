import pandas as pd

def load(path='/opt/airflow/data/wdbc-kaggle.csv'):
    df = pd.read_csv(path)
    print("Loaded", df.shape)
    return df