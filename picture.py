import easygopigo3 as easy
import time
import easypicamera
raspi_camera = easypicamera.EasyCamera()

sensor_readings = None

gpg = easy.EasyGoPiGo3() #instanciation de la classe GoPiGo

'dossier_photo'

photo_count = 1


easypicamera.create_folder_on_usb('dossier_photo') #création d'un dossier

raspi_camera.take_photo('dossier_photo'+'/'+'photo_3_'+str(photo_prise)+'.jpg') #prise d'une photo

photo_prise = photo_prise + 1 #incrémentation pour le nommage des photos
