import curses
import pyperclip
import webbrowser

from art_printer import draw_accounts_table
from db import DBSRC
from security import agent


class AccountManager():
    
    def __init__(self):
        self.accounts = DBSRC.list_accounts()

    def add_new_account(self, credentials: dict, sitename: str, link: str) -> None:
        DBSRC.add_account(agent.encrypt_credentials(credentials), sitename, link)

    def list_accounts(self) -> None:
        # decrypt credentials
        # delete 'credentails' key val pair in accounts
        # merge the new decrypted credentials dict into accounts
        if len(self.accounts) == 0: return
        for account in self.accounts:
            if "credentials" in account.keys():
                credentials = agent.decrypt_credentials(account["credentials"])
                account.pop("credentials", None)
                account.update(credentials)
        curses.wrapper(self.accounts_table_handler)
        
    def accounts_table_handler(self, stdscr: object) -> None:
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()

        current_row = 1
        draw_accounts_table(stdscr, current_row, self.accounts)
        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 1:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.accounts):
                current_row += 1
            elif key == ord('\n'):
                selected_account = self.accounts[current_row - 1]
                self.access_account_website(selected_account['link'])
            elif key == ord('c'):
                selected_account = self.accounts[current_row - 1]
                self.copy_account_credentials(selected_account['login'], selected_account['password'])
            elif key == 27:  # ESC key to exit
                break

            draw_accounts_table(stdscr, current_row, self.accounts)
    
    #Small helper methods
    def access_account_website(self, link: str) -> None:
        webbrowser.open(link)

    def copy_account_credentials(self, login: str, password: str) -> None:
        pyperclip.copy(f"Login: {login}, Password: {password}")

AM = AccountManager()
