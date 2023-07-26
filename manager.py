from getpass import getpass
from time import sleep
from os import system

from colorama import init
from colorist import Color
from InquirerPy import get_style, inquirer
from termcolor import cprint

def banner() -> None:
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
                                                                    
    """, 'blue')

def loading(text: str = 'loading', delay: float = .5) -> None:
    print('\033[1;34;40m', end=text)
    n_dots = 0

    while True:
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='\033[1;36;40m.', flush=True)
            n_dots += 1
        sleep(delay)

def verify() -> bool:
    cprint("Please enter the master password:", 'blue')
    pwd = getpass('')
    # TO DO: add an assertation for authentication when we add the DB.
    while pwd != 'test':
        cprint("That password isn't right. Please, re-enter your password:", 'red')
        pwd = getpass('')
    return True

def menu() -> None:
    if not verified:
        cprint('Unauthorized access!', 'red')
        exit(0)
    style = get_style({"questionmark": "#ffffff", "question": "#ffff00", "answer": "#008000", "pointer": "#61afef"}, style_override=False)
    actions = {"Check your accounts": 0, "Generate a temporairy email": 1, "Exit": 2}
    action = inquirer.select(
    message="Hello, How can I help you ?",
    choices= actions.keys(),
    style=style
    ).execute()
    if actions[action] == 0:
        verify()
        cprint("Fetching your accounts: ", "green")
        loading()
    if actions[action] == 2:
        if inquirer.confirm(message="Confirm?", default=True).execute():
            system('cls')
            exit(0)
        menu()

if __name__ == "__main__":
    init()
    banner()
    verified:bool = verify()
    menu()