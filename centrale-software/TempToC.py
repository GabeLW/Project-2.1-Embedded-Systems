Sensordata = '25'#voorbeeld

millivolts = int('0x'+ Sensordata, 16) * (5000 / 255)
print(millivolts)
    # 10 mv per degree
temp_C = ((millivolts - 100.0) / 10.0) - 40.0
    # remove decimal point from millivolts
millivolts = "%d" % millivolts
   # show only one decimal place for temprature and voltage readings
temp_C = "%.1f" % temp_C
print(temp_C)
