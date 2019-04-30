import easygopigo3 as easy
import time
import easypicamera
raspi_camera = easypicamera.EasyCamera()

sensor_readings = None

gpg = easy.EasyGoPiGo3()

'photo_folder'

photo_count = 1


easypicamera.create_folder_on_usb('photo_folder')

raspi_camera.take_photo('photo_folder'+'/'+'photo_3_'+str(photo_count)+'.jpg')

photo_count = photo_count + 1
