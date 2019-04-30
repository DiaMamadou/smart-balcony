import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

my_servo_portSERVO2 = gpg.init_servo('SERVO2')


# start
my_servo_portSERVO2.rotate_servo(10)