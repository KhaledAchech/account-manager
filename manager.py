from getpass import getpass
from os import system
from time import sleep
import subprocess

from config import set_file_permissions, MESSAGES, THEME, INQUIRER
from connector import database_connection, DB_INSTANT
from security import agent
from validation import assert_password

from colorama import init
from InquirerPy import get_style, inquirer
from termcolor import cprint


def banner() -> None:
    cprint(f"""
        .|'''|                                      ||                        
        ||                                    ''    ||                        
        `|'''|, .|''|, .|'', '||  ||` '||''|  ||  ''||''  '||  ||`            
         .   || ||..|| ||     ||  ||   ||     ||    ||     `|..||             
         |...|' `|...  `|..'  `|..'|. .||.   .||.   `|..'      ||             
                                                            ,  |'             
                                                             ''               
                 /.\                               ||                       ||    
                // \\                  ''          ||                       ||    
               //...\\    ('''' (''''  ||  ('''' ''||''   '''|.  `||''|,  ''||''  
              //     \\    `'')  `'')  ||   `'')   ||    .|''||   ||  ||    ||    
            .//       \\. `...' `...' .||. `...'   `|..' `|..||. .||  ||.   `|..' 
                                                                    
    """, THEME.get("default"))

def verify() -> bool:
    if (not agent.check_master_password()):
        cprint(MESSAGES.get("register_master_passowrd"), THEME.get("default"))
        pwd = getpass('')
        while not(assert_password(pwd)):
            pwd = getpass('')
        cprint(MESSAGES.get("confirm_master_password_registration"), THEME.get("default"))
        confirm = getpass('')
        while confirm != pwd:
            cprint(MESSAGES.get("wrong_master_password_confirmation"), THEME.get("error"))
            confirm = getpass('')
        agent.set_master_password(pwd)
    
    cprint(MESSAGES.get("ask_for_master_password"), THEME.get("default"))
    pwd = getpass('')
    while not(agent.verify_master_password(pwd)):
        cprint(MESSAGES.get("incorrect_master_password"), THEME.get("error"))
        pwd = getpass('')
    
    return True

def menu() -> None:
    if not verified:
        cprint(MESSAGES.get("unauthorized_access"), THEME.get("error"))
        exit(0)
    
    style = get_style(INQUIRER.get("props"), style_override=INQUIRER.get("override"))
    action = inquirer.select(
        message= MESSAGES.get("welcome_message"),
        choices= actions.keys(),
        style=style
    ).execute()
    
    if actions[action] == 0:
        verify()
        cprint(MESSAGES.get("fetch_accounts"), THEME.get("success"))
        subprocess.run(["python", "account_manager.py"])
    
    if actions[action] == 1:
        verify()
        subprocess.run(["python", "temp_email_manager.py"])
        menu()
    
    if actions[action] == -1:
        if inquirer.confirm(message=MESSAGES.get("confirmation"), default=True).execute():
            system('cls')
            if DB_INSTANT is not None:
                DB_INSTANT.close()
            exit(0)
        menu()

if __name__ == "__main__":
    init()
    banner()
    set_file_permissions()
    verified:bool = verify()
    database_connection()
    actions = {
        "Manage your accounts": 0,
        "Manage temporairy emails": 1,
        "Exit": -1
    }
    menu()
    DB_INSTANT.close()
