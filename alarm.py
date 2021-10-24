import time
from pygame import mixer

mixer.init()
mixer.music.load('A:/Sonstiges/Python Projects/pi_alarm/alarm_mp3/1.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)