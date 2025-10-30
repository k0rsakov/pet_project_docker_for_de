from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.docker.operators.docker import DockerOperator
import datetime

# Конфигурация DAG
OWNER = "i.korsakov"
DAG_ID = "compare_bash_vs_docker_operator"


LONG_DESCRIPTION = """
# LONG DESCRIPTION

"""

SHORT_DESCRIPTION = "SHORT DESCRIPTION"

args = {
    "owner": OWNER,
    "start_date": datetime.datetime(
        year=2025, month=10, day=20, tzinfo=datetime.timezone.utc
    ),
    "catchup": True,
    "retries": 3,
    "retry_delay": datetime.timedelta(hours=1),
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
        docker run --rm --rm \
          -e DB_HOST=BashOperator-prod-server-bash-{{ data_interval_start.format('YYYY-MM-DD') }} \
          -e DB_NAME=BashOperator-analytics_bash \
          -e DB_PORT=BashOperator-5432 \
          -e DB_USER=BashOperator-airflow_bash_user \
          simple_container_with_env
        """,
    )

    # Способ 2: Запуск через DockerOperator (нативно)
    run_via_docker_operator = DockerOperator(
        task_id="run_container_via_docker_operator",
        image="simple_container_with_env",
        auto_remove=True,
        environment={
            "DB_HOST": "DockerOperator-prod-server-docker-op-{{ data_interval_start.format('YYYY-MM-DD') }}",
            "DB_NAME": "DockerOperator-analytics_docker_op",
            "DB_PORT": "DockerOperator-5432",
            "DB_USER": "DockerOperator-airflow_docker_user",
        },
    )

    end = EmptyOperator(
        task_id="end",
    )

    # Запускаем параллельно для сравнения
    start >> [run_via_bash, run_via_docker_operator] >> end
