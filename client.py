import socket
from tkinter import *
import threading


def connect():
    host_ip = str(entHostIP.get())
    t1 = threading.Thread(target=transfer(host_ip))
    t1.daemon = True
    t1.start()


def transfer(host_ip):
    while True:
        s = socket.socket()
        host = host_ip
        port = 8000
        s.connect((host, port))

        s.send(b'Send File...')  # 1
        print("1. Client: Send File...")

        filename = s.recv(2048).decode()  # 2
        print("2. Server: File Name: " + str(filename))

        # path = "/storage/emulated/0/Download/Test2/" + str(filename)
        path = "./Test2/" + str(filename)
        s.send(b'Receiving File...')  # 3

        with open(path, 'wb') as f:
            print('File "' + str(filename) + '" opened')
            packet = 0
            while True:
                packet += 1
                print("Packet: " + str(packet))
                data = s.recv(2048)
                if not data:
                    break
                f.write(data)
        f.close()
        print("File Closed")
        s.close()
        print("3. Server: File Sent.")
        print("4. Client: Connection closed.\n")
        lblMessage['text'] = 'File "' + str(filename) + '" saved.'


if __name__ == '__main__':
    root = Tk()
    lblWelcome = Label(text="WiFi-Xfer Client")
    lblHostIp = Label(text="Host IP")
    entHostIP = Entry()
    btnConnect = Button(text="Connect", command=connect, width=10)
    lblMessage = Label(text="")

    lblWelcome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    lblHostIp.grid(row=2, column=1, padx=10, pady=10)
    entHostIP.grid(row=2, column=2, padx=10, pady=10)
    btnConnect.grid(row=3, column=1,  columnspan=2, padx=10, pady=10)
    lblMessage.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    root.title("WiFi-Xfer Client")
    root.mainloop()
