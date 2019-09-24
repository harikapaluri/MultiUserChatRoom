#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import asyncio
from multiprocessing import Process

client_socket = socket(AF_INET, SOCK_STREAM)

HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket.connect(ADDR)

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
            #msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send():  # event is passed by binders.
    """Handles sending of messages."""
    msg=input()
    client_socket.send(bytes(msg, "utf8"))
    if msg == "!q":
        client_socket.close()
        exit()
        #top.quit()
    send()

if __name__ == '__main__':
    Thread(target = receive).start()
    Thread(target = send).start()


'''loop= asyncio.get_event_loop()
try:
    asyncio.ensure_future(receive())
    asyncio.ensure_future(send())
    loop.run_forever()

except Exception:
    pass
finally:
    print("quitting")
    loop.close()'''