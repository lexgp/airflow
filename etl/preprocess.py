def preprocess(df):
    df = df.drop(['id', 'Unnamed: 32'], axis=1)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    X = df.drop('diagnosis', axis=1)
    y = df['diagnosis']
    return X, y
