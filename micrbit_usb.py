#You need to install the pyserial package to use the serial ports
import serial
import serial.tools.list_ports as list_ports
import time
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1


def find_comport(pid, vid, baud):
    
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None



print('looking for microbit')
ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser_micro:
    print('microbit not found')
else:    
    ser_micro.open()
    while True:
        data = str(ser_micro.readline())
        data = data.replace("b","")
        data = data.replace("'","")
        data = data.replace(" ","")
        data = data.replace("\\r\\n","")
        print(data)
        file=open("Textfile","w")
file.write(data)
file.close()