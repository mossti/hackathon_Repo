import serial
import time

ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600)
print ser.name

print('Enter servo 0 target:')
target0 = input()
targetTalk0 = 4*target0
lsb0 = targetTalk0 & 0x7F
msb0 = (targetTalk0 >> 7) & 0x7F

print('\nEnter servo 1 target:')
target2 = input()
targetTalk2 = 4*target2
lsb2 = targetTalk2 & 0x7F
msb2 = (targetTalk2 >> 7) & 0x7F


# We are using the compact mode
data0 = [0x84, 0x00, lsb0, msb0]
print data0
output0 = bytearray(data0)
print output0

data2 = [0x84, 0x02, lsb2, msb2]
print data2
output2 = bytearray(data2)
print output2

ser.write(output0)
ser.write(output2)

time.sleep(2)
ser.close()
