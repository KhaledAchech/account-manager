import psycopg2
from config import get_db_params, THEME
from termcolor import cprint

DB_PARAMS = get_db_params()
def server_connection() -> object:
    try:
        connection = psycopg2.connect(
            database=DB_PARAMS["default_database"],
            user=DB_PARAMS["user"],
            host=DB_PARAMS["host"],
            password=DB_PARAMS["password"],
            port=DB_PARAMS["port"]
        )
        connection.autocommit = True
    except psycopg2.Error as e:
        cprint(
            f"Error connecting to the PostgreSQL server: {e}", THEME.get("error"))
        exit(1)

    return connection
DB_SERVER = server_connection()


def database_exists() -> bool:
    cursor = DB_SERVER.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;",
                   (DB_PARAMS["database"],))
    exists = cursor.fetchone() is not None
    cursor.close()
    return exists

def database_connection() -> object:
    if not database_exists():
        try:
            cursor = DB_SERVER.cursor()
            cursor.execute(f"CREATE DATABASE {DB_PARAMS['database']};")
            cprint(f"Database '{DB_PARAMS['database']}' created successfully.", THEME.get(
                "success"))
        except psycopg2.Error as e:
            print(f"Error creating the database: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()

    # Connect to the existing or newly created database
    try:
        connection = psycopg2.connect(
            dbname=DB_PARAMS["database"],
            user=DB_PARAMS["user"],
            password=DB_PARAMS["password"],
            host=DB_PARAMS["host"],
            port=DB_PARAMS["port"]
        )
        cprint(
            f"Connected to database '{DB_PARAMS['database']}'.", THEME.get("success"))
    except psycopg2.Error as e:
        cprint(f"Error connecting to the database: {e}", THEME.get("error"))
        exit(1)
    return connection
DB_INSTANCE = database_connection()
