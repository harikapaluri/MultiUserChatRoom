from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
#Opening a socket connection from client side
clientConnection = socket(AF_INET, SOCK_STREAM)
PORT = int(input('Enter port: '))
HOST = input('Enter host: ')
#Buffer Size
BufferSize = 1024
ADDR = (HOST, PORT)
#Sending a request to the server to connect
clientConnection.connect(ADDR)
#Send function call for the client to send messages on the server.
def sendMessages(): 
     sendMessage=input()
     clientConnection.send(bytes(sendMessage, "utf8"))
     if sendMessage == "!q":         
        clientConnection.close()
        exit()
     sendMessages()
#Receive function  call for the client to receive messages from other clients connected to the server.
def recvMessages():
     while True:
        try:
            messageRecieved = clientConnection.recv(BufferSize ).decode("utf8")
            print(messageRecieved)
        except OSError:  #Chance of an exception arises if the client has decided to close his connection. 
            break

if __name__ == '__main__':
    Thread(target = recvMessages).start()
    Thread(target = sendMessages).start()
