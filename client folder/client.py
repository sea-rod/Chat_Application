import socket
import threading

class Client:

    __flag = True

    def __init__(self, host = "127.0.0.1", port = 8080, mess_size = 1024*128, head = 20) -> None:
        self.__host = host
        self.__port = port 
        self.mess_size = mess_size
        self.head = head
    

    def connect(self)->bool:
        '''
        connects to the server
        '''
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = self.__client.connect_ex((self.__host,self.__port))
        if code == 0:
            print(f"connected to {self.__host}:{self.__port}")
            self.t1 = threading.Thread(target = self.receive)
            self.t1.daemon = True
            self.t1.start()
            return True
        return False


    def receive(self)->None:
        '''
        Recevies from the server
        '''
        while self.__flag:
            mess = ''
            raw_mess = self.__client.recv(self.mess_size).decode()
            mess_len = int(raw_mess[:self.head])
            mess += str(raw_mess[self.head:])
            while len(mess) != mess_len:
                mess += self.__client.recv(self.mess_size).decode()
            print(mess)


    def send(self,mess:str)->bool:
        '''
        Sends to the server and the server sends to the user
        '''
        mess_head = f"{len(mess):{self.head}}"
        mess_head += mess
        self.__client.send(mess_head.encode())

        if mess == "quit":
            self.__flag = False
            return False

        return True

    def __del__(self):
        self.__client.close()