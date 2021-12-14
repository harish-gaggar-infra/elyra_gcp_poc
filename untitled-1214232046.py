from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "untitled-1214232046",
}

dag = DAG(
    "untitled-1214232046",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.3.0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'OzBttupc1gam1JlpOTmXwx7GP5uQ4lb5MFAB9S74' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="OzBttupc1gam1JlpOTmXwx7GP5uQ4lb5MFAB9S74",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="OzBttupc1gam1JlpOTmXwx7GP5uQ4lb5MFAB9S74",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: {'component-id': 'bash_operator.py'}
op_c8c57fff_def5_4fdd_9362_72b650a0e9ce = BashOperator(
    task_id="BashOperator",
    bash_command='echo "hello"',
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    dag=dag,
)
