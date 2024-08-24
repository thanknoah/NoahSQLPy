import socket

def sendRequest(msg, ip, port):
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_address = (ip, port)

   try:
       client_socket.connect(server_address)
       message = msg
       client_socket.sendall(message.encode('utf-8'))
       data = client_socket.recv(1024)
       print('Received response from server:', data.decode('utf-8'))
    
   finally:
       client_socket.close()

sendRequest("INSERT VALUES (2, 0) INTO userDetails", "127.0.0.1", 16032) # Example
