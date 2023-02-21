import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",9999))

is_done=False
while not is_done:
    client.send(input('Message: ').encode('utf-8'))
    msg=(client(client.recv(1024).decode('utf-8')))
    if msg=="quit":
        is_done=True
   else:
       print(msg)        
