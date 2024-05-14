
"""
@author: Nicolò Morini

"""
import socket
import threading
import requests

def ConnectToServer():

    server_ip = 'localhost'
    server_port = 8080

    socketObject = socket.socket()

    socketObject.connect((server_ip, server_port))

    print("Connected to:", server_ip)

    HTTPMessage = "GET /pagina_html_prova.html HTTP/1.1\r\n Connection: close\r\n\r\n"

    bytes = str.encode(HTTPMessage)

    socketObject.sendall(bytes)
    
    while(True):

        data = socketObject.recv(1024)
        print(data)
        if(data==b''):
            print("Connection closed")
            break
        
    socketObject.close()

print("Client - Main thread started") 
ThreadList  = []
ThreadCount = 20

for index in range(ThreadCount):

    ThreadInstance = threading.Thread(target=ConnectToServer())
    ThreadList.append(ThreadInstance)
    ThreadInstance.start()

for index in range(ThreadCount):

    ThreadList[index].join()