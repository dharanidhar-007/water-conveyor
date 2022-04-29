#!/usr/bin/python
import RPi.GPIO as GPIO
import time , sys
#import paho.mqtt.publish as publish

FLOW_SENSOR_GPIO = 13
#MQTT_SERVER = "192.168.1.220"

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1

GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = ((count * 10000) / 450)
        # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
        print("The flow is: %.2f ml/sec" % (flow))
        if flow > 0.00:
            i = int(count)
            j = int(count + 1)
            n = int(i+j)
            k = int((flow + flow) / n)
            print("The water consumed by the person is : %.2f" % (k))
        else:
            print("The water consumed by the person is : %.2f" % (flow))

        #publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
        count = 0
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nprocess killed..!!')
        GPIO.cleanup()
        sys.exit()
