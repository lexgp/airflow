import shutil
import os

def save():
    shutil.copy('/opt/airflow/results/model.pkl', '/opt/airflow/results/final_model.pkl')
    shutil.copy('/opt/airflow/results/metrics.json', '/opt/airflow/results/final_metrics.json')
