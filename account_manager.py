from config import THEME
from colorama import init
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
                                                                    
    """, THEME.get("default"))

if __name__ == "__main__":
    init()
    banner()