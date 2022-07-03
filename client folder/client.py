import socket
import threading

from matplotlib.ft2font import BOLD


class Client:

    __flag = True

    def __init__(self, host = "127.0.0.1", port = 8080, mess_size = 1024*128, head = 20) -> None:
        self.host = host
        self.port = port 
        self.mess_size = mess_size
        self.head = head
    

    def connect(self)->bool:
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = self.__client.connect_ex((self.host,self.port))
        if code == 0:
            print(f"connected to {self.host}:{self.port}")
            self.t1 = threading.Thread(target = self.receive)
            self.t1.daemon = True
            self.t1.start()
            return True
        return False


    def receive(self)->None:
        while self.__flag:
            mess = ''
            raw_mess = self.__client.recv(self.mess_size).decode()
            mess_len = int(raw_mess[:self.head])
            mess += str(raw_mess[self.head:])
            while len(mess) != mess_len:
                mess += self.__client.recv(self.mess_size).decode()
            print(mess)


    def send(self,mess:str)->bool:
        mess_head = f"{len(mess):{self.head}}"
        mess_head += mess
        self.__client.send(mess_head.encode())

        if mess == "quit":
            self.__flag = False
            return False

        return True


if __name__ == "__main__":

    con = Client()
    flag = con.connect()

    while flag:
        a = input()
        flag = con.send(a)