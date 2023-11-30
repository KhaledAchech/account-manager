import curses

from config import THEME
from termcolor import cprint
from colorama import init, Fore, Back

MAIL = Back.WHITE + Fore.BLUE

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

def temp_email_banner():
    cprint(f"""
        ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗                                                                          
        ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝                                                                          
        ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗                                                                            
        ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝                                                                            
        ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗                                                                          
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                                          
                                                                                                                                        
     ████████╗███████╗███╗   ███╗██████╗  ██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗    ███████╗███╗   ███╗ █████╗ ██╗██╗     ███████╗
     ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝
        ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║██████╔╝███████║██████╔╝ ╚████╔╝     █████╗  ██╔████╔██║███████║██║██║     ███████╗
        ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗██╔══██║██╔══██╗  ╚██╔╝      ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ╚════██║
        ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║██║  ██║██║  ██║   ██║       ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗███████║
        ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                    
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
    
    # Table Theme 
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Header color
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Even row color
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Odd row color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Selected row color
    
    stdscr.addstr(0, 0, "Login".ljust(20) + "Password".ljust(20) + "Sitename".ljust(30) + "Link", 
                  curses.A_BOLD | curses.color_pair(1))
    for i, account in enumerate(accounts, start=1):
        color_pair = curses.color_pair(2) if i % 2 == 0 else curses.color_pair(3)
        login = account['login'].ljust(20)
        password = ('○' * len(account['password'])).ljust(20)
        sitename = account['sitename'].ljust(30)
        link = account['link']
        stdscr.addstr(i, 0, f"{login}{password}{sitename}{link}",color_pair)
        if i == selected_row:
            stdscr.chgat(i, 0, curses.A_REVERSE | curses.color_pair(4))
    
    guide_text = "🔑Press 'C' to copy credentials  |  🚀Press 'Enter' to access a website  |  🏠Press 'ESC' to go back"
    stdscr.addstr(i + 2, 3, guide_text, curses.color_pair(1) | curses.A_BOLD | curses.A_ITALIC)

    stdscr.refresh()
