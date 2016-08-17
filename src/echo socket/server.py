import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5000))
server_socket.listen(5)

print ("TCPServer Waiting for client on port 5000")

client_socket, address = server_socket.accept()
print ("I got a connection from ", address)


while 1:
    data = client_socket.recv(512).decode()
    if(data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print ("RECEIVED:" , data)

server_socket.close()
print("SOCKET closed... END")