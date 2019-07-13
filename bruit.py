import easygopigo3 as easy
import time
# create an EasyGoPiGo3 object
gpg = easy.EasyGoPiGo3()
# and now instantiate a LoudnessSensor object through the gpg3_obj object
capteur_son = gpg.init_loudness_sensor(port='AD1') #instanciation du capteur et indication du port sur lequel il est connecté

for count in range(10):
    valeur = capteur_son.read()	#lecture des données envoyés par le capteur
    pourcentage = capteur_son.percent_read()	#lecture des données en pourcentage
    print(valeur)	#affichage des données
    print(pourcentage)	#affichage des données en pourcentage
    time.sleep(2)	#repos de deux seconde avant chaque affichage