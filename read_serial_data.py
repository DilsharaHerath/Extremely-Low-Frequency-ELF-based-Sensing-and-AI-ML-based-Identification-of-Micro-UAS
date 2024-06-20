#Method 2

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []

for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))

val = input('Select Port: COM')

for x in range(0, len(portlist)):
    if portlist[x].startswith('COM'+str(val)):
        portVar = 'COM' + str(val)
        print(portlist[x])

# Set the baud rate
serialInst.baudrate = 50000
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))
