#!/usr/bin/python3   
      
import time
import serial
               
ser = serial.Serial(            
    port='/dev/rfcomm0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)
         
 
#ser.write(b'Hello\n')
time.sleep(7)

while 1:
    data = 'a'
    data=data.encode('UTF-8')
    ser.write(data)
    time.sleep(1)
