from microbit import *

red = pin2
green = pin1
blue = pin0

while True:
  red.write_digital(1)
  sleep(2000) # punainen valo päälle ja odotusta 2 sekuntia
  
  red.write_digital(0) # Mitä tapahtuu, jos tätä riviä ei kirjoita?
  blue.write_digital(1)
  sleep(2000)
  
  # Värin asteittainen lisääminen tapahtuu seuraavasti. Mitä koodi mahtaa tehdä?
  blue.write_digital(0)
  sleep(1000)
  red.write_digital(1)
  for i in range (0, 1023):
    green.write_analog(i)
    sleep(10)
  sleep(2000) 
 
  # Lopuksi valot pois päältä ennen kuin while True -silmukka alkaa alusta uudelleen
  red.write_digital(0)
  blue.write_digital(0)
  green.write_digital(0)
