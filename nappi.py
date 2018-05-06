from microbit import *

while True:
  if button_a.is_pressed:
    pin1.write_digital(1) # pin1 "menee päälle"
  else:
    pin1.write_digital(0) # "pois päältä"
  
  if pin0.is_touched: #rakenna pin0:sta nappi kytkemällä sen ja gnd:n välille johto
    pin1.write_digital(1)
  else:
    pin1.write_digital(0)
