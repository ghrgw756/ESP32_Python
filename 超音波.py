from machine import Pin
import machine
import time
echoTimeount = 23200
trigpin = Pin(17,mode=Pin.OUT)
echopin = Pin(16,mode=Pin.OUT)

def distance():
    trigpin.value(1)
    time.sleep_us(10)
    trigpin.value(0)
    pulseTime=machine.time_pulse_us(echopin,1,echoTimeount)
    if pulseTime>0:
        return pulseTime/58
    else:
        return pulseTime

while True:
    cm = distance()
    if(cm > 0):
        print("distance :",cm)
    else:
        print("distance =",cm)
    time.sleep(1)