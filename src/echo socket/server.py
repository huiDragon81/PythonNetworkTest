import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_socket.bind(("localhost", 5000));
server_socket.listen();

client_socket, address = server_socket.accept();
print ("connection from : ", address);

while 1:
    data = client_socket.recv(512).decode();
    if(data == 'q' or data == 'Q'):
        client_socket.close();
        break;
    else:
        print ("recv from : " , data);

server_socket.close();
print("socket close");