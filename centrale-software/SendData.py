import serial
from time import sleep
import struct
from ctypes import c_uint8
ser = serial.Serial('COM5', 9600)
print(ser)
sleep(5)

ser.write(c_uint8(int('0x0b', 16)))
sleep(5)
ser.write(c_uint8(int('0x0a', 16)))
