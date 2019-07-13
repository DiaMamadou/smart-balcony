import easygopigo3 as easy
import time
import time
from di_sensors import easy_inertial_measurement_unit

sensor_readings = None

gpg = easy.EasyGoPiGo3()

try:
    my_imu_portAD2= easy_inertial_measurement_unit.EasyIMUSensor(port='AD1')
    time.sleep(0.2)
except:
    print('Inertial Measurement Unit not responding')
    time.sleep(0.2)
    exit()


# start
start_time = time.time()
while time.time() - start_time < 1:
    pass
    time.sleep(0.05) # slowdown
print(my_imu_portAD2.convert_heading(int(my_imu_portAD2.safe_read_euler()[int(0)])))
time.sleep(0.2)
