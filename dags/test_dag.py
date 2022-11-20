# test_dag.py
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import yesterday

dag = DAG(
    dag_id="test",
    schedule_interval=None,
    start_date=yesterday("Asia/Seoul")
)


def test_callable():
    print(os.getcwd())
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    print(os.path.join(os.environ['_GCS_BUCKET']))

test = PythonOperator(task_id='test',
                      python_callable=test_callable,
                      dag=dag)


# dependency
test