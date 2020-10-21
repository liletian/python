import serial.tools.list_ports as port_list
ports = list(port_list.comports())
for p in ports:
    print (p)


import serial

#s = serial.Serial('COM3')

ser = serial.Serial('COM4', 115200, timeout=1)

ser.write(str.encode('w0103'))
ser.write(str.encode('w027c'))
ser.write(str.encode('w0080'))

ser.write(str.encode('r'))
ser.write(str.encode('06'))
a=ser.read(2)






while True:
    for line in ser.read():

        print(str(count) + str(': ') + chr(line) )
        count = count+1

ser.close()

