from machine import Pin
import socket
import network,utime
Pin26 = Pin(26,Pin.OUT)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
while True:
    print('wificonnection')
    try:
        wifi.connect('Lee_living room','aaa88888')
        if wifi.isconnected():
            print('Network Config=',wifi.ifconfig())
            data = wifi.ifconfig()
            break
    except :
        print('error')
    utime.sleep(1)
print(data)
host = data[0] #127.0.0.1:1024~65535
port = 5487
s=socket.socket()
s.bind((host,port))
s.listen(1)
print(host,"is openning at",port)
client,addr = s.accept()
print("client address",addr[0],'port',addr[1])
while True:
    if msg == 'hi':
        reply = b'hello'
    elif msg == 'quit':
        client.send(b'quit')
    elif msg == 'opengreen':
        Pin26.value(1)
        client.send(b'The green light is haven open')
    else:
        reply = b'i dont know'

client.close()