from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
    }
    with open('results/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
