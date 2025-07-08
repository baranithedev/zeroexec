from .ansicolors import *
def custom_banner(func):
    def wrapper(*args, **kwargs):
        text=f"""███████╗███████╗██████╗  ██████╗ ███████╗██╗  ██╗███████╗ ██████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝╚██╗██╔╝██╔════╝██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║█████╗   ╚███╔╝ █████╗  ██║     
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══╝   ██╔██╗ ██╔══╝  ██║     
███████╗███████╗██║  ██║╚██████╔╝███████╗██╔╝ ██╗███████╗╚██████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝

[GITHUB]: @BARANITHEDEV \t[AUTHOR]: @BaraniDharan
[INSTAGRAM]: https://www.instagram.com/mr._.sudo/
"""

        print(f"{SOFT_GREEN}{text}{RESET}")
        return func(*args, **kwargs)
    return wrapper

@custom_banner
def tagline():
    after_border="[*] Not a user. Not a defender. I’m the exploitator.\n"
    tagline=after_border.upper()
    return f"{SOFT_GREEN}{tagline}{RESET}"
