from getpass import getpass
from os import system
from time import sleep
import subprocess

from config import set_file_permissions, MESSAGES, THEME, INQUIRER
from connector import database_connection, DB_INSTANT

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

# def loading(text: str = 'loading', delay: float = .5) -> None:
#     print('\033[1;34;40m', end=text)
#     n_dots = 0

#     while True:
#         if n_dots == 3:
#             print(end='\b\b\b', flush=True)
#             print(end='   ',    flush=True)
#             print(end='\b\b\b', flush=True)
#             n_dots = 0
#         else:
#             print(end='\033[1;36;40m.', flush=True)
#             n_dots += 1
#         sleep(delay)

def verify() -> bool:
    cprint(MESSAGES.get("ask_for_master_password"), THEME.get("default"))
    pwd = getpass('')
    # TO DO: add an assertation for authentication when we add the DB and code needs refactoring.
    while pwd != 'test':
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
        # loading()
    
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
