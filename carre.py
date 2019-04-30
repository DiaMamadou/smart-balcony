import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

left_motor_target = 360
right_motor_target = 360

#gpg.reset_encoders(blocking=True)
# start

gpg.drive_cm(-50)
gpg.turn_degrees(-90)
gpg.drive_cm(-30)
gpg.turn_degrees(-90)
gpg.drive_cm(-50)
gpg.turn_degrees(-90)
gpg.drive_cm(-30)
gpg.turn_degrees(-90)


#while gpg.target_reached(left_motor_target, right_motor_target):
    #time.sleep(1)
    #gpg.stop()
    #gpg.drive_degrees(-90)
#time.sleep(20)
#gpg.stop()


import easygopigo3 as easy
import time
gpg = easy.EasyGoPiGo3()
my_servo_portSERVO2 = gpg.init_servo('SERVO2')

for count in range (4) :
    my_servo_portSERVO2.rotate_servo(90)
    gpg.drive_cm(-50)
    gpg.turn_degrees(-90)