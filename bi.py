import easygopigo3 as easy
import time
from di_sensors.easy_light_color_sensor import EasyLightColorSensor

gpg = easy.EasyGoPiGo3()
my_servo_portSERVO2 = gpg.init_servo('SERVO2')
capteur_son = gpg.init_loudness_sensor(port='AD1')
detection_mouvement=gpg.init_motion_sensor('AD2')
raspi_camera = easypicamera.EasyCamera()
distance_1 = gpg.init_distance_sensor()

'dossier_photo'

photo_count = 1


easypicamera.create_folder_on_usb('dossier_photo')

for count in range (480) :
    my_servo_portSERVO2.rotate_servo(110)
    gpg.drive_cm(55)
    gpg.turn_degrees(-100)
    gpg.drive_cm(10)
    gpg.turn_degrees(-100
	time.sleep(60)

for count in range(480):

	pourcentage = capteur_son.percent_read()
    time.sleep(2)

    if detection_mouvement.motion_detected():	#conditionnement si il y'a un mouvement
        raspi_camera.take_photo('dossier_photo'+'/'+'photo_3_'+str(photo_prise)+'.jpg')
        photo_prise = photo_prise + 1

    else if (pourcentage>=50):
        raspi_camera.take_photo('dossier_photo'+'/'+'photo_3_'+str(photo_prise)+'.jpg')
        photo_prise = photo_prise + 1