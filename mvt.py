import easygopigo3 as easy
import time
# create an EasyGoPiGo3 object
gpg = easy.EasyGoPiGo3()
detection_mouvement=gpg.init_motion_sensor('AD2')	#instanciation du capteur et indication du port sur lequel il est connecté

for count in range(30):
    time.sleep(2)
    if detection_mouvement.motion_detected():	#conditionnement si il y'a un mouvement
        print('mouvement')	#affichage s'il y'a mouvement
    else:
        print('pas de mouvement')	#affichage s'il ya pas de mouvement