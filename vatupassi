from microbit import *

while True:
   # ohakee kiihtyvyysanturin x-arvon
   x = accelerometer.get_x()
   
   # jakaa arvon, jotta anturi olisi vähemmän herkkä
   val = x // 20
   
   if val > 0:
      display.show(Image.ARROW_E)
   elif x < 0:
      display.show(Image.ARROW_W)
   else:
      display.show(Image.YES)
