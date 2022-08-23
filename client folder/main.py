from client import Client
import socket




try:
    ip = input("Enter the host name or ip address:")
    port = int(input("Enter the port:"))
    ip = socket.gethostbyname(ip)
    clt = Client(ip,port)
    flag = clt.connect()
    while flag:
        mess = input()
        flag = clt.send(mess)

except socket.gaierror:
    print("Please a enter a valid ip or host name and try again")

    
except ValueError:
    print("Port number should be a integer")

