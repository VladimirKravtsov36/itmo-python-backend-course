import psycopg2

DATABASE_URL = "postgresql://pguser:pgpassword@db:5432/db"


def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


# Create a table if it doesn't exist
def create_experiments_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS experiments (
            id SERIAL PRIMARY KEY,
            model_name VARCHAR(255),
            task VARCHAR(255),
            dataset VARCHAR(255),
            metric_name VARCHAR(255),
            metric_value FLOAT
        );
    """
    )
    conn.commit()
    conn.close()
