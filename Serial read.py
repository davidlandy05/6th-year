import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

while True:

    mb_temperature = str(ser.readline().decode('utf-8'))
    print(len(mb_temperature))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    print("Len of temp is: ", len(mb_temperature))
    print(mb_temperature)
    if mb_temperature.isdigit():
        print("Write to fb")
    else:
        print("Check data source")