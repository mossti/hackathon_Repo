import serial
import time

ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600)
print ser.name
manipMain = True

while manipMain == True:
    print('Enter servo 0 target:')
    target0 = input()
    targetTalk0 = 4*target0
    lsb0 = targetTalk0 & 0x7F
    msb0 = (targetTalk0 >> 7) & 0x7F

    print('\nEnter servo 2 target:')
    target2 = input()
    targetTalk2 = 4*target2
    lsb2 = targetTalk2 & 0x7F
    msb2 = (targetTalk2 >> 7) & 0x7F


    # We are using the compact mode
    data0 = [0x84, 0x00, lsb0, msb0]
    print data0
    output0 = bytearray(data0)
    #print output0

    data2 = [0x84, 0x02, lsb2, msb2]
    print data2
    output2 = bytearray(data2)
    #print output2

    ser.write(output0)
    ser.write(output2)

    print "\nWould you like to continue? [y=1/n=0]"
    manipMainQuery = input()
    if manipMainQuery == 1:
        manipMain = True
    if manipMainQuery == 0:
        manipMain = False

dataReset0 = [0x84, 0x00, 0x70, 0x2E]
dataReset2 = [0x84, 0x02, 0x70, 0x2E]
outputReset0 = bytearray(dataReset0)
outputReset2 = bytearray(dataReset2)

ser.write(outputReset0)
ser.write(outputReset2)

time.sleep(2)
ser.close()
