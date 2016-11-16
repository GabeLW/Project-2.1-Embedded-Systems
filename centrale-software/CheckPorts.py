import serial
import warnings
import serial.tools.list_ports

arduino_ports = [
    p.device for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
    ]

if not arduino_ports:
    print('No Arduino Found!@#!@#@!')
if len(arduino_ports) > 1:
       print('Meerdere Arduinos!!@!#!@')
       print('Aantal aangesloten apparaten: ' + str(x+1))

ser = serial.Serial(arduino_ports[0],  9600)
print(ser)
while True:
    s = ser.read()
    print('Temperatuur: ' + s.hex())
