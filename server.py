import os
import socket
from tkinter import *
from tkinter import filedialog


def transfer(filepaths):
    if filepaths == "" or filepaths is None:
        print("No file path found.")
        return

    lblMessage['text'] = ""
    for filepath in filepaths:
        path, filename = os.path.split(filepath)
        print("1. File Name: " + str(filename))
        while True:
            conn, addr = s.accept()
            print("2. Server: Connection from: ", addr)

            message = conn.recv(2048).decode()  # 1
            print("3. Client: ", str(message))

            conn.send(filename.encode())  # 2
            print("4. Server: File Name Sent")

            data = conn.recv(2048).decode()  # 3
            print("5. Client: ", str(data))

            f = open(filepath, 'rb')
            data = f.read(2048)
            while data:
                conn.send(data)
                data = f.read(2048)
            f.close()

            print('6. File Received.\n')
            conn.close()
            lblMessage['text'] += "File Sent: " + filename + "\n"
            print("Select File...")
            break


def select_files():
    files = filedialog.askopenfilenames(initialdir="./", title="Select File",
                                        filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
    transfer(files)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip = str(sock.getsockname()[0])
    sock.close()

    host = "0.0.0.0"
    port = 8000
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print('\nServer listening....')
    print("Select File...")

    root = Tk()
    lblWelcome = Label(text="WiFi-Xfer Server")
    lblIp = Label(text="Host IP")
    lblIpValue = Label(text=ip)
    lblSelect = Label(text="Select File")
    btnSelect = Button(text="Select", command=select_files, width=10)
    lblMessage = Label(text="")

    lblWelcome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    lblIp.grid(row=2, column=1, padx=10, pady=10)
    lblIpValue.grid(row=2, column=2, padx=10, pady=10)
    lblSelect.grid(row=3, column=1, padx=10, pady=10)
    btnSelect.grid(row=3, column=2, padx=10, pady=10)
    lblMessage.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    root.title("WiFi-Xfer Server")
    root.mainloop()
