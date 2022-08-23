from server import Server
import socket


try:
    ip = input("Enter the host name or ip address you to bind the server with:")
    port = int(input("Enter the port:"))
    ip = socket.gethostbyname(ip)
    srv = Server(ip,port)
    srv.listen()
    srv.accept()


except socket.gaierror:
    print("Please a enter a valid ip or host name and try again")

    
except ValueError:
    print("Port number should be a integer")





