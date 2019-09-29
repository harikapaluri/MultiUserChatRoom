from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

client_socket = socket(AF_INET, SOCK_STREAM)

HOST = input('Enter host: ')
PORT = int(input('Enter port: '))

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket.connect(ADDR)

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
        except OSError:  # Possibly client has left the chat.
            break

def send():  # event is passed by binders.
    """Handles sending of messages."""
    msg=input()
    client_socket.send(bytes(msg, "utf8"))
    if msg == "!q":
        client_socket.close()
        exit()
    send()

if __name__ == '__main__':
    Thread(target = receive).start()
    Thread(target = send).start()
