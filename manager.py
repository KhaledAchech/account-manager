from getpass import getpass
from os import system
from time import sleep
import subprocess

from config import set_file_permissions, ACTIONS, MESSAGES, THEME, INQUIRER
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

def temp_email_manager() -> None:
    cprint(f"""
        ______  ___                                                                                                              
        ___   |/  /_____ _____________ _______ _____                                                                             
        __  /|_/ /_  __ `/_  __ \  __ `/_  __ `/  _ \                                                                            
        _  /  / / / /_/ /_  / / / /_/ /_  /_/ //  __/                                                                            
        /_/  /_/  \__,_/ /_/ /_/\__,_/ _\__, / \___/                                                                             
                               /____/                                                                                    
       _____                                            _____                                          ___________       
       __  /____________ ______________________________ ___(_)___________  __   ____________ _________ ___(_)__  /_______
       _  __/  _ \_  __ `__ \__  __ \  __ \_  ___/  __ `/_  /__  ___/_  / / /   _  _ \_  __ `__ \  __ `/_  /__  /__  ___/
       / /_ /  __/  / / / / /_  /_/ / /_/ /  /   / /_/ /_  / _  /   _  /_/ /    /  __/  / / / / / /_/ /_  / _  / _(__  ) 
       \__/ \___//_/ /_/ /_/_  .___/\____//_/    \__,_/ /_/  /_/    _\__, /     \___//_/ /_/ /_/\__,_/ /_/  /_/  /____/  
                            /_/                                     /____/                                               
                                                                    
    """, THEME.get("default"))
    temp_emails_menu()

def account_manager() -> None:
    cprint(f"""
        █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝ 
        ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║    
        ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║    
        ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║    
        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝    
                                                                    
            ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
            ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
            ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
            ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
            ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                    
    """, THEME.get("default"))
    cprint(MESSAGES.get("fetch_accounts"), THEME.get("success"))
    # actions = ACTIONS.get("account_manager")

def main_menu() -> None:
    if not verified:
        cprint(MESSAGES.get("unauthorized_access"), THEME.get("error"))
        exit(0)
    
    actions = ACTIONS.get("security_assistant")
    style = get_style(INQUIRER.get("props"), style_override=INQUIRER.get("override"))
    action = inquirer.select(
        message= MESSAGES.get("security_assistant_welcome_message"),
        choices= actions.keys(),
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
            if DB_INSTANT is not None:
                DB_INSTANT.close()
            exit(0)
        main_menu()

def temp_emails_menu():
    actions = ACTIONS.get("temp_emails_manager")
    style = get_style(INQUIRER.get("props"), style_override=INQUIRER.get("override"))
    action = inquirer.select(
        message= MESSAGES.get("temp_emails_manager_welcome_message"),
        choices= actions.keys(),
        style=style
    ).execute()
    
    if actions[action] == 0:
        verify()
    
    if actions[action] == 1:
        verify()
    
    if actions[action] == -1:
        if inquirer.confirm(message=MESSAGES.get("confirmation"), default=True).execute():
            system('cls')
            return

if __name__ == "__main__":
    init()
    banner()
    set_file_permissions()
    verified:bool = verify()
    database_connection()
    main_menu()
    DB_INSTANT.close()
