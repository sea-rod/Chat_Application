from client import Client

clt = Client()
flag = clt.connect()

while flag:
    mess = input()
    flag = clt.send(mess)

if not flag:
    print("Connection failed retry!!")