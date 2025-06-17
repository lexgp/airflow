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

# 1. Загрузка данных
def step_1_load(**context):
    df = load()
    context['ti'].xcom_push(key='df', value=df)

# 2. Предобработка
def step_2_preprocess(**context):
    df = context['ti'].xcom_pull(key='df', task_ids='load_data')
    X, y = preprocess(df)
    context['ti'].xcom_push(key='X', value=X)
    context['ti'].xcom_push(key='y', value=y)

# 3. Обучение
def step_3_train(**context):
    X = context['ti'].xcom_pull(key='X', task_ids='preprocess')
    y = context['ti'].xcom_pull(key='y', task_ids='preprocess')
    model, X_test, y_test = train(X, y)
    context['ti'].xcom_push(key='model', value=model)
    context['ti'].xcom_push(key='X_test', value=X_test)
    context['ti'].xcom_push(key='y_test', value=y_test)

# 4. Оценка
def step_4_evaluate(**context):
    model = context['ti'].xcom_pull(key='model', task_ids='train')
    X_test = context['ti'].xcom_pull(key='X_test', task_ids='train')
    y_test = context['ti'].xcom_pull(key='y_test', task_ids='train')
    evaluate(model, X_test, y_test)

# 5. Сохранение
def step_5_save(**context):
    model = context['ti'].xcom_pull(key='model', task_ids='train')
    save(model)

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
