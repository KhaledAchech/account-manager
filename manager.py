import pyperclip

from getpass import getpass
from os import system

from art_printer import security_assistant_banner, account_banner, temp_email_banner, draw_mail_box
from config import set_file_permissions, ACTIONS, MESSAGES, THEME, INQUIRER
from connector import database_connection, DB_INSTANCE
from security import agent
from validation import assert_password
from account import AM
from temp_email import create_email, check_mail

from colorama import init
from InquirerPy import get_style, inquirer
from termcolor import cprint


def verify() -> bool:
    if (not agent.check_master_password()):
        cprint(MESSAGES.get("register_master_passowrd"), THEME.get("default"))
        pwd = getpass('')
        while not (assert_password(pwd)):
            pwd = getpass('')
        cprint(MESSAGES.get("confirm_master_password_registration"),
               THEME.get("default"))
        confirm = getpass('')
        while confirm != pwd:
            cprint(MESSAGES.get("wrong_master_password_confirmation"),
                   THEME.get("error"))
            confirm = getpass('')
        agent.set_master_password(pwd)

    cprint(MESSAGES.get("ask_for_master_password"), THEME.get("default"))
    pwd = getpass('')
    while not (agent.verify_master_password(pwd)):
        cprint(MESSAGES.get("incorrect_master_password"), THEME.get("error"))
        pwd = getpass('')

    return True


def account_manager() -> None:
    account_banner()
    # cprint("TO BE CONTINUED ... ☻", THEME.get("warning"))
    account_menu()


def account_menu() -> None:
    actions = ACTIONS.get("account_manager")
    action = inquirer.select(
        message=MESSAGES.get("account_manager_welcome_message"),
        choices=actions.keys(),
        style=style
    ).execute()
    if actions[action] == 0:
        # verify()
        add_account()

    if actions[action] == 1:
        # verify()
        get_accounts()

    if actions[action] == -1:
        if inquirer.confirm(message=MESSAGES.get("confirmation"), default=True).execute():
            system('cls')
            return

def add_account():
    login = input("Type in the login for this account: ")
    print("Type in the new account password: ")
    password = getpass()
    sitename = input("Type in the app name for this account: ")
    link = input("Paste in the link of this app: ")
    credentials = {
        "login": login,
        "password": password
    }
    AM.add_new_account(credentials, sitename, link)
    # the same inquirer behaviour for asking for another account to add or going back

def get_accounts():
    AM.list_accounts()

def temp_email_manager() -> None:
    temp_email_banner()
    temp_emails_menu()

def temp_emails_menu() -> None:
    actions = ACTIONS.get("temp_emails_manager")
    action = inquirer.select(
        message=MESSAGES.get("temp_emails_manager_welcome_message"),
        choices=actions.keys(),
        style=style
    ).execute()

    if actions[action] == 0:
        verify()
        set_temp_email()

    if actions[action] == 1:
        verify()
        fetch_mail()

    if actions[action] == -1:
        if inquirer.confirm(message=MESSAGES.get("confirmation"), default=True).execute():
            system('cls')
            return

def set_temp_email() -> None:
    login, domain, = None, None
    if inquirer.confirm(message=MESSAGES.get("custom_login_question"), default=True).execute():
        cprint(MESSAGES.get("custom_login_input"), THEME.get("default"))
        login = input()
    if inquirer.confirm(message=MESSAGES.get("custom_domain_question"), default=True).execute():
        cprint(MESSAGES.get("custom_domain_input"), THEME.get("default"))
        domain = input()
    mail = create_email(login, domain)
    cprint(MESSAGES.get("success"), THEME.get("success"))
    cprint(MESSAGES.get("temp_email_address") + mail, THEME.get("default"))
    pyperclip.copy(mail)
    cprint(MESSAGES.get("copied_to_clipboard"), THEME.get("success"))
    if inquirer.confirm(message=MESSAGES.get("create_another_email"), default=True).execute():
        set_temp_email()
    temp_email_manager()

def fetch_mail(mail: str = None) -> None:
    if not mail:
        cprint(MESSAGES.get("enter_mail"), THEME.get("default"))
        mail = input()
    mails = check_mail(mail)
    for m in mails:
        for key, value in m.items():
            if key == "Subject":
                subject = value
            if key == "Sender":
                sender = value
            if key == "Content":
                content = value
        recipient = mail
        draw_mail_box(sender, recipient, subject, content)
    if inquirer.confirm(message=MESSAGES.get("refresh_mail_box"), default=True).execute():
        fetch_mail(mail)
    temp_email_manager()

def main_menu() -> None:
    if not verified:
        cprint(MESSAGES.get("unauthorized_access"), THEME.get("error"))
        exit(0)

    actions = ACTIONS.get("security_assistant")
    action = inquirer.select(
        message=MESSAGES.get("security_assistant_welcome_message"),
        choices=actions.keys(),
        style=style
    ).execute()

    if actions[action] == 0:
        verify()
        account_manager()
        main_menu()

    if actions[action] == 1:
        verify()
        temp_email_manager()
        main_menu()

    if actions[action] == -1:
        if inquirer.confirm(message=MESSAGES.get("confirmation"), default=True).execute():
            system('cls')
            if DB_INSTANCE is not None:
                DB_INSTANCE.close()
            exit(0)
        main_menu()


if __name__ == "__main__":
    init()
    security_assistant_banner()
    set_file_permissions()
    verified: bool = verify()
    database_connection()
    style = get_style(INQUIRER.get("props"),
                      style_override=INQUIRER.get("override"))
    main_menu()
    DB_INSTANCE.close()
