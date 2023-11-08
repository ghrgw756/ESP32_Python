from machine import Pin, SoftI2C
import ssd1306

SDA_PIN = 17
SCL_PIN = 16

# using SoftI2C
i2c = SoftI2C(sda=Pin(SDA_PIN), scl=Pin(SCL_PIN))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text('SSD130s886 OL=999===ED', 0, 0)
display.text('with', 0, 16)
display.text('MicroPython', 0,32)

display.show()
