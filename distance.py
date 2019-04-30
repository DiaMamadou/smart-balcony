import easygopigo3 as easy
import time
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

distance_1 = gpg.init_distance_sensor('I2C')
time.sleep(0.1)


# start
while not distance_1.read_inches() < 10:
    gpg.forward()
    time.sleep(0.05)
gpg.stop()
