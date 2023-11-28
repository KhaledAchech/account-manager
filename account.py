import curses
import pyperclip
import webbrowser

from art_printer import draw_accounts_table
from db import DBSRC
from security import agent

ACCOUNTS = []


def add_new_account(credentials: dict, sitename: str, link: str) -> None:
    DBSRC.add_account(agent.encrypt_credentials(credentials), sitename, link)


def list_accounts() -> None:
    # decrypt credentials
    # delete 'credentails' key val pair in accounts
    # merge the new decrypted credentials dict into accounts
    ACCOUNTS = DBSRC.list_accounts()
    for account in ACCOUNTS:
        credentials = agent.decrypt_credentials(account["credentials"])
        account.pop("credentials", None)
        account.update(credentials)
    curses.wrapper(accounts_table_handler)


def access_account_website(link: str) -> None:
    webbrowser.open(link)


def copy_account_credentials(login: str, password: str) -> None:
    pyperclip.copy(f"Login: {login}, Password: {password}")


def accounts_table_handler(stdscr: object) -> None:
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    current_row = 1
    draw_accounts_table(stdscr, current_row, ACCOUNTS)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 1:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(ACCOUNTS):
            current_row += 1
        elif key == ord('\n'):
            selected_account = ACCOUNTS[current_row - 1]
            access_account_website(selected_account['link'])
        elif key == ord('c'):
            selected_account = ACCOUNTS[current_row - 1]
            copy_account_credentials(
                selected_account['login'], selected_account['password'])
        elif key == 27:  # ESC key to exit
            break

        draw_accounts_table(stdscr, current_row, ACCOUNTS)
