import curses

from config import THEME
from termcolor import cprint
from colorama import init, Fore, Back

MAIL = Back.WHITE + Fore.BLUE


def account_banner():
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


def security_assistant_banner():
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


def temp_email_banner():
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


def draw_mail_box(sender: str, recipient: str, subject: str, content: str) -> None:
    # Determine the maximum line width
    content_lines = content.split('\n')
    max_line_length = max(len(sender), len(recipient), len(
        subject), max(len(line) for line in content_lines))

    # Create the top and bottom parts of the mailbox
    top = "+-" + "-" * max_line_length + "-+\n"
    middle = MAIL + \
        f"|SENDER: {sender.ljust(max_line_length)}|\n|TO: {recipient.ljust(max_line_length)}|\n|SUBJECT: {subject.ljust(max_line_length)}|\n"
    init(autoreset=True)
    bottom = "+-" + "-" * max_line_length + "-+\n"

    # Split the content into lines and format each line
    content_box = MAIL + ""
    for line in content_lines:
        content_box += f"|  {line.ljust(max_line_length)}  |\n"

    mailbox = top + middle + bottom + content_box + bottom
    init(autoreset=True)
    cprint(mailbox, THEME.get("box"))


def draw_accounts_table(stdscr: object, selected_row: int, accounts: list) -> None:
    stdscr.clear()

    stdscr.addstr(0, 0, "Login\tPassword\tSitename\tLink", curses.A_BOLD)

    for i, account in enumerate(accounts, start=1):
        stdscr.addstr(
            i, 0, f"{account['login']}\t{'☻'*len(account['password'])}\t{account['sitename']}\t{account['link']}")
        if i == selected_row:
            stdscr.chgat(i, 0, curses.A_REVERSE)

    stdscr.refresh()
