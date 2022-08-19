This a small chat application. Where a client can send and receive messages.

If both the sever and tht client script are on the same system. Then you just start the
it by running the sever script first then the client script.


If the client and server are on different system which are in the same network then
you need to run the server script and specify the port as "0.0.0.0"
You can specify the port and host in the script where the server object is initialized: 
srv = Server(host = "0.0.0.0",port = 8080)
To close the servevr to need press ctrl+c.

To run the client script you need to specify the host to the server's ip
You can specify the client port and host in the script where the client object is initialized:
clt = Client(host = "<the server's ip>",port = 8080)

Remember the server and client port need to be same !!! 

