from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "demo7-1213214340",
}

dag = DAG(
    "demo7-1213214340",
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


# Operator source: 1.ipynb
op_de5e7b17_eb60_4a22_bc53_e705caaea2fd = KubernetesPodOperator(
    name="1",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint https://storage.googleapis.com --cos-bucket elyrapoc --cos-directory 'demo7-1213214340' --cos-dependencies-archive '1-de5e7b17-eb60-4a22-bc53-e705caaea2fd.tar.gz' --file '1.ipynb' --outputs '1' "
    ],
    task_id="1",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "demo7-1213214340-{{ ts_nodash }}",
    },
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: 2.ipynb
op_803933cb_0c9e_4cdf_82a0_85be89525fbb = KubernetesPodOperator(
    name="2",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint https://storage.googleapis.com --cos-bucket elyrapoc --cos-directory 'demo7-1213214340' --cos-dependencies-archive '2-803933cb-0c9e-4cdf-82a0-85be89525fbb.tar.gz' --file '2.ipynb' --inputs '1' --outputs '2.csv' "
    ],
    task_id="2",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "demo7-1213214340-{{ ts_nodash }}",
    },
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_803933cb_0c9e_4cdf_82a0_85be89525fbb << op_de5e7b17_eb60_4a22_bc53_e705caaea2fd
