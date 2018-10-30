from microbit import *

# tämä käynnistää kompassin kalibroinnin. Täytä ruutu kääntelemällä, kunnes näet hymiön :)
compass.calibrate()

while True:
   sleep(100)
   val = compass.heading()
   if (val < 10 or val > 350):
      # micro:bit osoittaa pohjoiseen
      display.show('N')
   else:
      display.show(Image.NO) # näyttää rastin
      
   # Lisää kompassiissi muutkin ilmansuunnat
