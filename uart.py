import serial.tools.list_ports as port_list
ports = list(port_list.comports())
for p in ports:
    print (p)


import serial

s = serial.Serial('COM3')


ser = serial.Serial(port, 115200, timeout=1)

