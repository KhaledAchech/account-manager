import psycopg2

from connector import DB_INSTANCE
from config import THEME, MESSAGES
from termcolor import cprint

ACCOUNT_TABLE_INIT = '''CREATE TABLE IF NOT EXISTS account (
    account_id SERIAL PRIMARY KEY,
    credentials BYTEA NOT NULL,
    sitename VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL
);'''


class DB():
    def __init__(self, instance):
        self.instance = instance
        self.create_table_account()

    def create_table_account(self):
        try:
            with self.instance.cursor() as cursor:
                cursor.execute(ACCOUNT_TABLE_INIT)
            cprint("[DB Operations]: Account table initialized with success!",
                   THEME.get("success"))
        except psycopg2.Error as e:
            cprint(
                f"[DB Operations]: Error creating table account: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()

    def add_account(self, credentials: bytes, sitename: str, link: str) -> None:
        try:
            with self.instance.cursor() as cursor:
                cursor.execute("INSERT INTO account (credentials, sitename, link) values(%s, %s, %s);",
                               (memoryview(credentials), sitename, link)
                               )
            self.instance.commit()
            cprint("[DB Operations]: Account saved with success!",
                   THEME.get("success"))
        except psycopg2.Error as e:
            cprint(
                f"[DB Operations]: Error inserting a new row into account: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()

    def list_accounts(self) -> list:
        results = []
        try:
            with self.instance.cursor() as cursor:
                cursor.execute("SELECT * FROM ACCOUNT;")
                data = cursor.fetchall()
                for row in data:
                    results.append({
                        "credentials": bytes(row[1]),
                        "sitename": row[2],
                        "link": row[3]
                    })
            cprint(MESSAGES.get("fetch_accounts"), THEME.get("success"))
        except psycopg2.Error as e:
            cprint(
                f"[DB Operations]: Error fetching accounts: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()
        return results


DBSRC = DB(DB_INSTANCE)
