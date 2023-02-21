import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serve.bind(('localhost',9999))
server.listen()
client,addr=server.accept()
is_done=False

while not is_done:
    msg=print(client.recv(1024).decode('utf-8'))
    if msg=="quit":
        is_done=True
    else:
        print(msg)        
    client.send(input('Message: ').encode('utf-8'))
