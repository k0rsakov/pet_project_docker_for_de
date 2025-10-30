from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.docker.operators.docker import DockerOperator

# Конфигурация DAG
OWNER = "i.korsakov"
DAG_ID = "compare_bash_vs_docker_operator"


LONG_DESCRIPTION = """
# LONG DESCRIPTION

"""

SHORT_DESCRIPTION = "SHORT DESCRIPTION"

args = {
    "owner": OWNER,
    "start_date": pendulum.datetime(2023, 1, 1, tz="Europe/Moscow"),
    "catchup": True,
    "retries": 3,
    "retry_delay": pendulum.duration(seconds=1),
}

with DAG(
    dag_id=DAG_ID,
    schedule_interval="20 4 * * *",
    default_args=args,
    tags=["docker"],
    description=SHORT_DESCRIPTION,
    concurrency=1,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:
    dag.doc_md = LONG_DESCRIPTION

    start = EmptyOperator(
        task_id="start",
    )

    run_via_bash = BashOperator(
        task_id="run_container_via_bash",
        bash_command="""
        docker run \
          -e DB_HOST=prod-server-bash \
          -e DB_NAME=analytics_bash \
          -e DB_PORT=5432 \
          -e DB_USER=airflow_bash_user \
          simple_container_with_env
        """,
    )

    # Способ 2: Запуск через DockerOperator (нативно)
    run_via_docker_operator = DockerOperator(
        task_id="run_container_via_docker_operator",
        image="simple_container_with_env",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={
            "DB_HOST": "prod-server-docker-op",
            "DB_NAME": "analytics_docker_op",
            "DB_PORT": "5432",
            "DB_USER": "airflow_docker_user",
        },
    )

    end = EmptyOperator(
        task_id="end",
    )

    # Запускаем параллельно для сравнения
    start >> [run_via_bash, run_via_docker_operator] >> end
