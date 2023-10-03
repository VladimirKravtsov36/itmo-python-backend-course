import psycopg2
import psycopg2.extras

from .create import get_db
from schemas.experiment import Experiment


class DBManager:
    def __init__(self):
        self.conn = get_db()
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


class ExperimentsManager(DBManager):
    def create_experiment(self, experiment: Experiment):
        self.cursor.execute(
            """
            INSERT INTO experiments (model_name, task, dataset, metric_name, metric_value)
            VALUES (%(model_name)s, %(task)s, %(dataset)s, %(metric_name)s, %(metric_value)s)
            RETURNING id;
            """,
            experiment.model_dump(),
        )

        new_experiment_id = self.cursor.fetchone()["id"]
        self.conn.commit()
        self.conn.close()
        return {"id": new_experiment_id}

    def read_experiments(self):
        self.cursor.execute("SELECT * FROM experiments")

        experiments = self.cursor.fetchall()
        self.conn.close()

        return experiments

    def get_experiment_by_id(self, experiment_id: int):
        self.cursor.execute(
            "SELECT * FROM experiments WHERE id = %s;", (experiment_id,)
        )
        db_result = self.cursor.fetchone()
        self.conn.close()

        return db_result


class MetricManager(DBManager):
    def get_metric_for_dataset(self, dataset: str, metric_name: str):
        self.cursor.execute(
            """
            SELECT *
            FROM experiments
            WHERE dataset = %s AND metric_name = %s;
        """,
            (dataset, metric_name),
        )

        experiments = self.cursor.fetchall()
        self.conn.close()

        return experiments

    def get_models_for_task(self, task: str, dataset: str, metric_name: str):
        self.cursor.execute(
            """
            SELECT *
            FROM experiments
            WHERE task = %s AND dataset = %s AND metric_name = %s;
        """,
            (task, dataset, metric_name),
        )

        experiments = self.cursor.fetchall()
        self.conn.close()

        return experiments
