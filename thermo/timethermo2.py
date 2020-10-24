#!/usr/bin/python3
from RPLCD.gpio import CharLCD, GPIO
import time
from datetime import datetime
import w1thermsensor

print("Start")
lcd = CharLCD(cols=16, rows=2, pin_rs=22, pin_e=18, pins_data=[16, 15, 13, 11],numbering_mode=GPIO.BOARD)
sensor = w1thermsensor.W1ThermSensor()

def print_data():
    num_cols=16
    temp_string = str(round(sensor.get_temperature(),1)) +" "+chr(223)+"C"
    dt_string = datetime.now().strftime("%H:%M:%S")
    lcd.home()
    lcd.write_string(temp_string.ljust(num_cols)[:num_cols])
    lcd.write_string('\r\n')
    lcd.write_string(dt_string.ljust(num_cols)[:num_cols])
            
try:
    while True:
        print_data()
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
lcd.close(clear=True)
print("End")