def custom_banner(func):
    def wrapper(*args, **kwargs):
        text=f"""
███████╗███████╗██████╗  ██████╗ ███████╗██╗  ██╗███████╗ ██████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝╚██╗██╔╝██╔════╝██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║█████╗   ╚███╔╝ █████╗  ██║     
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══╝   ██╔██╗ ██╔══╝  ██║     
███████╗███████╗██║  ██║╚██████╔╝███████╗██╔╝ ██╗███████╗╚██████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝

GitHub: #baranithedev\tInstagram:  @mr_.sudo
"""
        print(f"{text}")
        result=func(*args, **kwargs)
        return result
    return wrapper

@custom_banner
def tagline():
    after_border="[*] Not a user. Not a defender. I’m the exploitator.\n"
    tagline=after_border.upper()
    return f"{tagline}"
