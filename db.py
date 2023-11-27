import psycopg2

from connector import DB_INSTANCE
from config import THEME
from termcolor import cprint

import secrets

ACCOUNT_TABLE_INIT = '''CREATE TABLE IF NOT EXISTS account (
    account_id SERIAL PRIMARY KEY,
    login VARCHAR(255) NOT NULL,
    hashed_password BYTEA NOT NULL,
    sitename VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL
);'''


class DB():
    def __init__(self, instance):
        self.instance = instance

    def create_table_account(self):
        try:
            with self.instance.cursor() as cursor:
                cursor.execute(ACCOUNT_TABLE_INIT)
        except psycopg2.Error as e:
            cprint(
                f"Error creating table account: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()

    def add_account(self, login: str, hashed_password: bytes, sitename: str, link: str) -> None:
        try:
            with self.instance.cursor() as cursor:
                cursor.execute("INSERT INTO account (login, hashed_password, sitename, link) values(%s, %s, %s, %s);",
                               (login, hashed_password, sitename, link)
                               )
            self.instance.commit()
        except psycopg2.Error as e:
            cprint(
                f"Error inserting a new row into account: {e}", THEME.get("error"))
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
                        "id": row[0],
                        "login": row[1],
                        "hashed_password": row[2],
                        "sitename": row[3],
                        "link": row[4]
                    })
        except psycopg2.Error as e:
            cprint(
                f"Error fetching accounts: {e}", THEME.get("error"))
            exit(1)
        finally:
            cursor.close()
        return results


# just for now for quick tests; will be deleted spoon :p
if __name__ == "__main__":
    db = DB(DB_INSTANCE)
    db.create_table_account()
    db.add_account("test", secrets.token_bytes(16),
                   "simple test", "www.test.com")
    db.add_account("test2", secrets.token_bytes(16),
                   "simple test2", "www.test2.com")
    db.add_account("test3", secrets.token_bytes(16),
                   "simple test3", "www.test3.com")
    data = db.list_accounts()
    cprint(data, THEME.get("default"))
