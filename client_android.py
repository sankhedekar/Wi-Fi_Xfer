import socket

try:
    host = input("Enter Host IP Address: ")  # Get local machine name
    while True:
        s = socket.socket()     # Create a socket object
        port = 8000            # Reserve a port for your service.
        s.connect((host, port))

        s.send(b'Send File...')  # 1
        print("1. Client: Send File...")

        filename = s.recv(2048).decode()  # 2
        print("2. Server: File Name: " + str(filename))

        path = "/storage/emulated/0/Download/" + str(filename)
        s.send(b'Receiving File...')  # 3

        with open(path, 'wb') as f:
            print('File "' + str(filename) + '" opened')
            packet = 0
            while True:
                packet += 1
                # print("Packet: " + str(packet))
                data = s.recv(2048)
                if not data:
                    break
                # write data to a file
                f.write(data)
        f.close()
        print("File Closed")
        s.close()
        print("3. Server: File Sent.")
        print("4. Client: Connection closed.\n")


except Exception as e:
    print("Error: " + str(e))
