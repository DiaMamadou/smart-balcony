import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()


# start
gpg.reset_encoders(blocking=True)
