from RPLCD.gpio import CharLCD, GPIO
print("Start")
lcd = CharLCD(cols=16, rows=2, pin_rs=22, pin_e=18, pins_data=[16, 15, 13, 11],numbering_mode=GPIO.BOARD)
#lcd.write_string(u'test')
#raw_input ("Continue...")
#lcd.write_string(u'test')
#raw_input ("Continue...")
bstring = u'Cześć Łukasz!'
lcd.write_string(bstring)
text =raw_input (">")
lcd.write_string(text)
raw_input ("Press any key to terminate the program")
lcd.close(clear=True)
print("End")
