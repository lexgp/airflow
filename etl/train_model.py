from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def train(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    joblib.dump(model, '/opt/airflow/results/model.pkl')
    return model, X_test, y_test
