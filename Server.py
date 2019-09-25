from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def incoming():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to SHH Chat server, now enter your name and join!", "utf8"))
        Thread(target=new_client, args=(client,client_address)).start()


def new_client(client,address): 

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type !q to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("!q", "utf8"):
            broadcast(msg, "->"+name+": ")
        else:
            client.send(bytes("!q", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            print("%s:%s has discconnected." % address)
            break


def broadcast(msg, prefix=""):  
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = int(input("Enter port number: "))
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Accepting Connections...")
    ACCEPT = Thread(target=incoming)
    ACCEPT.start()
    ACCEPT.join()
    SERVER.close()