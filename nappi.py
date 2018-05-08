from microbit import *

while True:
  if button_a.is_pressed():
    pin1.write_digital(1) # pin1 "menee päälle"
  else:
    pin1.write_digital(0) # "pois päältä"
  
#rakenna halutessasi pin0:sta "nappi" kytkemällä sen ja gnd:n välille johto
  if pin0.is_touched(): 
    pin1.write_digital(1)
  else:
    pin1.write_digital(0)
    
#Tai näin:
#    if something is True:
#    # do one thing
#elif some other thing is True:
#    # do another thing
#else:
#    # do yet another thing.
    
