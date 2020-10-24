#!/usr/bin/python3
from RPLCD.gpio import CharLCD, GPIO
import time
print("Start")
lcd = CharLCD(cols=16, rows=2, pin_rs=22, pin_e=18, pins_data=[16, 15, 13, 11],numbering_mode=GPIO.BOARD)

lcd.write_string('Czesc Lukasz!')
text =input ("Wypisz tekst wprowadzony>")
lcd.write_string(text)
input('Smiley')
#własne znaki
smiley = (
0b00000,
0b01010,
0b01010,
0b00000,
0b10001,
0b10001,
0b01110,
0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string('\x00')
input('Test scrolla - ctrl+c exit')
framebuffer = [
    'Test scrolla',
    '',
]
def write_to_lcd(lcd, framebuffer, num_cols):
    """Write the framebuffer out to the specified LCD."""
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')
def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.2):
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)
try:
    while True:
        loop_string('testowy dlugi napis abcd', lcd, framebuffer, 1, 16)
except KeyboardInterrupt:
    pass
lcd.close(clear=True)
print("End")
