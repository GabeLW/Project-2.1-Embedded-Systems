import serial
from ctypes import c_uint8
from time import sleep
ser = serial.Serial('COM5', 9600)
sleep(3)
print(ser)
while True:
    sleep(2)
    for x in range(2):
        ser.write(c_uint8(int(0)))
        s = ser.read()
        if (s.hex() == '0a'):
            s = ser.read()
            print('Lichtintensiteit is: ' + s.hex())
        elif (s.hex() == '0b'):
            s = ser.read()
            print('Tempereatuur is : ' + s.hex())
