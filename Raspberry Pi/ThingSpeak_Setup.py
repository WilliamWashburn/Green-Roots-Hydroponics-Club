#1-wire interface needs to be enabled in rasp pi config menu


import os
import glob
import sys
import urllib2
from time import sleep

# Enter Your API key here
myAPI = '35B62ZTSPFHP2F7P' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

print('set up complete')

def ds18b20_data_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def ds18b20_data():
    lines = ds18b20_data_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

while True:
    try:
        print('trying to do job')
        temp = ds18b20_data()
		print(temp)

        # If Reading is valid
        if isinstance(temp, float):
            # Formatting to two decimal places
            temp = '%.2f' % temp
            

            print('Sending the data to thingspeak')
            conn = urllib2.urlopen(baseURL + '&field1=%s' % temp)
            conn.read()
            print("hello")
                                               
            # Closing the connection
            conn.close()

        else:
            print('Error')

        sleep(20)

    except Exception as e: print(e)

