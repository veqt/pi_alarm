import os
from datetime import *
import time
import pyttsx3

os.system('mpg321 -g 20 ./alarm_mp3/9-45.mp3 &')

# mixer.init()
# mixer.music.load('./alarm_mp3/9-45.mp3')
# mixer.music.play()
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)

startingTime = datetime.now()
endingTime = startingTime
endingTime = endingTime.replace(hour=0, minute=11, second=0)
if endingTime < startingTime:
    endingTime += timedelta(days=1)

while datetime.now() < endingTime:
    time.sleep(1)

# mixer.init()
# mixer.music.load('./alarm_mp3/1.mp3')
# mixer.music.play()
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)

os.system('mpg321 -g 20 1.mp3 &')

