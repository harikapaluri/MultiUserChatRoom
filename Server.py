from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

#Function for accepting incoming client connections
def incoming():
    #A loop that waits forever till it gets a client connection
    while True:
        server,clientList = SERVER.accept()
        print("%s:%s has connected." % clientList)
        server.send(bytes("Welcome to SHH Chat server, enter your name and join the room!", "utf8"))
        Thread(target=new_client, args=(server,clientList)).start()

#Function for connecting with a new client in order to recieve and send messages to and from server
def new_client(newclient,address): 
    #Client enters name which has to be recieved by server. 
    nameOfClient = newclient.recv(BUFSIZ).decode("utf8")
    #Welcome message from the server
    welcome = 'Hello %s! If you ever want to quit , type !q to log out of the chat room.' % nameOfClient
    #Server sending a welcome message to the client
    newclient.send(bytes(welcome, "utf8"))
    msg = "%s has joined the room!" % nameOfClient
    #Sending a broadcast message that is visible to all the clients conected over the chat room.
    messageBroadcast(bytes(msg, "utf8"))
    #Saving all client names in a dictionary
    listOfClients[newclient] = nameOfClient

    while True:
        msg = newclient.recv(BUFSIZ)
        if msg != bytes("!q", "utf8"):
            messageBroadcast(msg, "->"+nameOfClient+": ")
        else:
            newclient.send(bytes("!q", "utf8"))     #New client is sending !q to the server inorder to quit the chat room.
            newclient.close()
            del listOfClients[newclient]          #Closing connection for new client and deleting name entry from clients dictionary.
            messageBroadcast(bytes("%s has left the chat room." % nameOfClient, "utf8"))
            print("%s:%s has logged out ." % address)
            break


#Function for Broadcasting message that has to be sent to all existing Client connections of the server.
def messageBroadcast(message, nameId=""):  
    for socketConn in listOfClients:
        socketConn.send(bytes(nameId, "utf8")+message)

#A Dictionary of client names       
listOfClients = {}
#A Dictionary of client IP's
listOfAddresses = {}

HOST = ''
PORT = int(input("Enter port number: "))
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
#Binding host address to open a socket connection
SERVER.bind(ADDR)

if __name__ == "__main__":
    #Server listening for client requests here we have mentioned atmost 5 requests.
    SERVER.listen(5)
    print("Listening for incoming connections....")
    ACCEPT = Thread(target=incoming)
    ACCEPT.start() #Start of the main thread which starts the infinite loop.
    ACCEPT.join()  #The main thread wait's till the child thread that is Accept completes its execution.
    SERVER.close()
