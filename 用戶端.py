import socket
s=socket.socket() 
s.connect(('192.168.68.66',5487))
while True:
    msg = input("what is your message?")
    s.send(msg.encode('utf-8'))
    reply = s.recv(128)
    if reply == b'quit':
        print("close connect")
        s.close()
        break
    print(str(reply))