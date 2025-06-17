import sys
sys.path.append('/opt/airflow')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.load_data import load
from etl.preprocess import preprocess
from etl.train_model import train
from etl.evaluate import evaluate
from etl.save_results import save

def step_1_load():
    global df
    df = load()

def step_2_preprocess():
    global X, y
    X, y = preprocess(df)

def step_3_train():
    global model, X_test, y_test
    model, X_test, y_test = train(X, y)

def step_4_evaluate():
    evaluate(model, X_test, y_test)

def step_5_save():
    save()

with DAG(
    dag_id='ml_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    t1 = PythonOperator(task_id='load_data', python_callable=step_1_load)
    t2 = PythonOperator(task_id='preprocess', python_callable=step_2_preprocess)
    t3 = PythonOperator(task_id='train', python_callable=step_3_train)
    t4 = PythonOperator(task_id='evaluate', python_callable=step_4_evaluate)
    t5 = PythonOperator(task_id='save_results', python_callable=step_5_save)

    t1 >> t2 >> t3 >> t4 >> t5
