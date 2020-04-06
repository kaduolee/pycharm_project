
from PIL import ImageGrab
import time
 
n = 0
box = (50,50,800,640)
while n<10:
    im = ImageGrab.grab(box)
    im.save('1.jpg','jpeg')
    im.show()
    n += 1
    time.sleep(10)
