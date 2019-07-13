	import easygopigo3 as easy
# create an EasyGoPiGo3 object
gpg = easy.EasyGoPiGo3()
# and now instantiate a LoudnessSensor object through the gpg3_obj object
loudness_sensor = gpg.init_loudness_sensor()
# do the usual stuff, like read the data of the sensor
value = loudness_sensor.read()
value_percentage = loudness_sensor.percent_read()

if value>10:
    print("Test passed.")