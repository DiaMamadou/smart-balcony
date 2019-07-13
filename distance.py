import easygopigo3 as easy
import time
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

distance_1 = gpg.init_distance_sensor('I2C')	#instanciation du capteur et indication du port sur lequel est connecté celui-ci
time.sleep(0.1)

while not distance_1.read_inches() < 10:
    gpg.forward()	#faire avancer le gopigo
    time.sleep(0.05)
gpg.stop()	#arreter le gopigo