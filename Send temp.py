import time
import firebase_admin
import serial
from firebase_admin import credentials
from firebase_admin import db

ser=serial.Serial()
ser.buadrate = 115200
ser.port = "COM5"
ser.open()


cred=credentials.Certifacate("C:/Users/18DLandy.ACC/Downloads/test-f4bef-firebase-adminsdk-op3ae-3b6ce776cf.json")
databaseURL: "https://test-f4bef-default-rtdb.europe-west1.firebasedatabase.app"

ref= db.reference()
ref.update({'temperature_log'})
ref = db.reference().child('temperature_log')

source= input("Please input the source of this data:")
i=0
while True:
    
    mb_temperature = str(ser.readline().decide('utf-8'))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\m","")
    
    if mb_temperature.isdigit():
        ref.update({"Reading" + str(i):{'Temperature':mb_temperature, 'Location':source}})
        i = i+1
    
        
                         
                   