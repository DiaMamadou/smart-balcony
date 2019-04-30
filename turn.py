import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()


# start
gpg.forward()
time.sleep(1)
gpg.stop()
gpg.turn_degrees(-90, blocking=True)
gpg.stop()
