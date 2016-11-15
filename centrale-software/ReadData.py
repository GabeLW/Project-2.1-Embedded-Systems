import serial
import ctypes import c_uint8
from time import sleep
ser = serial.Serial('COM4', 9600)
print(ser)
while True:
    ser.write(c_uint8(int(0)))
    s = ser.read()
    if (s.hex() == '00'):
        s = ser.read()
        print('Lichtintensiteit is: ' + s.hex())
    elif (s.hex() == 'ff'):
        s = ser.read()
        print('Tempereatuur is : ' + s.hex())
