#Method 1

import serial

ser = serial.Serial(port = '', baurdrate = 50000) # path to the port

while True:
    value = ser.readline()
    valueInString = str(value, 'UTF-8')
    print(valueInString) 

