import easygopigo3 as easy
import time
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

leson = gpg.init_loudness_sensor('AD1')


# start
value = leson.read()
value_percentage = leson.percent_read()

----------------------------
import easygopigo3 as easy
import time
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

leson = gpg.init_loudness_sensor('AD1')


# start
for count in range(10):
    value = leson.read()
    value_percentage = leson.percent_read()
    #sleep(30)

---------------------------------

import easygopigo3 as easy
import time
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

leson = gpg.init_loudness_sensor('AD1')


# start
start_time = time.time()
while time.time() - start_time < 360:
    pass
    time.sleep(0.05) # slowdown
    value = leson.read()
    value_percentage = leson.percent_read()
    #sleep(30)

------------------------------------
/rootfs/media/DISK_IMG/

-----------------------------------
f=open("/media/DISK_IMG/textR.txt", "w")
values = str(value)
f.write(values)
f.close
----------------------------------------
import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

leson = gpg.init_loudness_sensor('AD1')

valuess = ""
# start
f=open("/media/DISK_IMG/valeursRetournees.txt", "w")
while time.time() - start_time < 300:
    value = leson.read()
    value_percentage = leson.percent_read()
    #values = values+"\n"+value
    
    values = str(value)
    valuess = valuess +"\n"+values
f.write(valuess)
f.close()
    #sleep(30)
#-----
import easygopigo3 as easy
import time

sensor_readings = None

gpg = easy.EasyGoPiGo3()

leson = gpg.init_loudness_sensor('AD1')

valuess
# start
start_time = time.time()
f=open("/media/DISK_IMG/valeursRetournees.txt", "w")
while time.time() - start_time < 1:
    value = leson.read()
    #value_percentage = leson.percent_read()
    #values = values+"\n"+value
    
    values = str(value)
    valuess = valuess +"\n"+values
f.write(valuess)
f.close()
    #sleep(30)
#-----