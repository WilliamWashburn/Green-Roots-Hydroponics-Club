#1-wire interface needs to be enabled in rasp pi config menu

import time
from w1thermsensor import W1ThermSensor
import sys
import urllib2
from time import sleep

# Enter Your API key here
myAPI = 'HV3D80PIDIJX6GSV' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

#This is for the temp sensor
sensor = W1ThermSensor()

def ds18b20_data():
	temp = sensor.get_temperature() 
	return temp

while True:
	try:
		temp = ds18b20_data()

		# If Reading is valid
		if isinstance(temp, float):
			# Formatting to two decimal places
			temp = '%.2f' % temp
			
			print temp
			# Sending the data to thingspeak
			#conn = urllib2.urlopen(baseURL + '&field1=%s' % temp
			#print conn.read()
                                               
			# Closing the connection
			#conn.close()

		else:
			print 'Error'

		sleep(20)

	except:
		break
