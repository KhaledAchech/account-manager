from connector import DB_INSTANCE
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
        with self.instance.cursor() as cursor:
            cursor.execute(ACCOUNT_TABLE_INIT)

    def add_account(self, login: str, hashed_password: bytes, sitename: str, link: str) -> None:
        with self.instance.cursor() as cursor:
            cursor.execute("INSERT INTO account (login, hashed_password, sitename, link) values(%s, %s, %s, %s);",
                           (login, hashed_password, sitename, link)
                           )
        self.instance.commit()


# just for now for quick tests; will be deleted spoon :p
if __name__ == "__main__":
    db = DB(DB_INSTANCE)
    db.create_table_account()
    db.add_account("test", secrets.token_bytes(16),
                   "simple test", "www.test.com")
