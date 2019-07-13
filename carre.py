import easygopigo3 as easy
import time
gpg = easy.EasyGoPiGo3()
my_servo_portSERVO2 = gpg.init_servo('SERVO2')

for count in range (2) :
    my_servo_portSERVO2.rotate_servo(110)
    gpg.drive_cm(55)
    gpg.turn_degrees(-100)
    gpg.drive_cm(10)
    gpg.turn_degrees(-100)



    import easygopigo3 as easy
import time
gpg = easy.EasyGoPiGo3()
my_servo_portSERVO2 = gpg.init_servo('SERVO2')

#for count in range (2) :
    #my_servo_portSERVO2.rotate_servo(90)
gpg.drive_cm(30)
gpg.turn_degrees(-100)
gpg.drive_cm(10)
gpg.turn_degrees(-100)
    
gpg.drive_cm(30)
gpg.turn_degrees(-100)
gpg.drive_cm(10)
gpg.turn_degrees(-100)