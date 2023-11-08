import socket
host = '192.168.68.66' #127.0.0.1:1024~65535
port = 5487
s=socket.socket()
s.bind((host,port))
s.listen(1)
print(host,"is openning at",port)
client,addr = s.accept()
print("client address",addr[0],'port',addr[1])
while True:
    msg = client.recv(128).decode('utf-8')
    print("client just send message :",msg)
    reply = ''
    if msg == 'hi':
        reply = b'hello'
    elif msg == 'quit':
        client.send(b'quit')
    else:
        reply = b'i dont know'
    client.send(reply)

client.close()