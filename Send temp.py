import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db

ser=serial.Serial()
ser.buadrate = 115200
ser.port = "COM4"
ser.open()


cred=credentials.Certificate("C:/Users/18DLandy.ACC/Downloads/test-f4bef-firebase-adminsdk-op3ae-43b882ee7c.json")
firebase_admin.initialize_app(cred)reference

ref= db.reference()
ref.update({'temperature_log'})
ref = db.reference().child('temperature_log')

source= input("Please input the source of this data:")
i=0
while True:
    
    mb_temperature = str(ser.readline().decide('utf-8'))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\m","")
    mb_temperature = str(ser.readline().decide('utf-8'))
    if mb_temperature.isdigit():
        ref.update({"Reading" + str(i):{'Temperature':mb_temperature, 'Location':source}})
        i = i+1

        
                         
                   