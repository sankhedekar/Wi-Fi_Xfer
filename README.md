# Wi-Fi Xfer (Currently under development)

Transfer files between different devices (PC/Laptop and Android) on same network using Python.

Server file can only be run on windows laptop while respective client files can be run on respective devices(windows or android).

# To transfer files between PC's/Laptops on the same network.
First run server_WifiXfer.py file and then client_windows.py
Get the Host IP address from the server_WifiXfer.py and enter it on client_windows.py and click on connect.
Select the file which you want to transfer on server_WifiXfer.py
Multiple files can be selected.


# To transfer files between PC/Laptop and Android on the same network.
Python simulator is required to run the client_android.py file on Android.
I have used "QPython3 - Python3 for Android" of "QPythonLab" from Google Play Store to run the program on Android but you can use any other simulators.
Check if your internal storage has "Download" folder, if not then create a new one or else it will give an error while executing the program on Android.
First run server_WifiXfer.py file and then client_android.py.
Get the Host IP address from the server.py and enter it on client_android.py and click on connect.
Select the file which you want to transfer on server_WifiXfer.py
Multiple files can be selected.

(Working on Android to send and recieve files from PC/Laptop)
