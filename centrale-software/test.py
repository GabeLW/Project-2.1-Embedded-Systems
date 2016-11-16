#pip install pyserial
import serial
ser = serial.Serial('COM4',  19200)
print(ser)
while True:
    s = ser.read()
    print(s.hex())
