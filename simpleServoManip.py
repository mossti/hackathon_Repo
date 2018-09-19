import serial
import time

ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600)
print ser.name

print('Enter servo 0 target:')
target0 = input()
targetTalk0 = 4*target
lsb0 = targetTalk0 & 0x7F
msb0 = (targetTalk0 >> 7) & 0x7F
print('Enter servo 1 target:')
target1 = input()


# We are using the compact mode
data = [0x84, 0x00, lsb0, msb0]
print data
output = bytearray(data)
print output
ser.write(output)

time.sleep(2)
ser.close()
