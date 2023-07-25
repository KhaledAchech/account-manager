from getpass import getpass
from time import sleep

from colorama import init
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
    print(end=text)
    n_dots = 0

    while True:
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
        sleep(delay)

def verify() -> bool:
    pwd = getpass("Please enter the master password:")
    # TO DO: add an assertation for authentication when we add the DB.
    assert pwd == 'test'
    return True

def menu() -> None:
    if not verified:
        cprint('Unauthorized access!', 'red')
        exit(0)
    style = get_style({"questionmark": "#ffffff", "answer": "#000000",  "pointer": "#61afef"}, style_override=False)
    actions = {"Check your accounts": 0, "Generate a temporairy email": 1, "Exit": 2}
    action = inquirer.select(
    message="Hello, How can I help you ?",
    choices= actions.keys(),
    style=style
    ).execute()
    if actions[action] == 0:
        cprint('We require re-authentication for this action', 'blue')
        verify()
        cprint("Fetching your accounts: ", "blue")
        loading()
    if actions[action] == 2:
        if inquirer.confirm(message="Confirm?", default=True).execute():
            exit(0)
        menu()

if __name__ == "__main__":
    init()
    banner()
    verified:bool = verify()
    menu()