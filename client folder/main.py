from client import Client

clt = Client()
flag = clt.connect()

while flag:
    mess = input()
    flag = clt.send(mess)
