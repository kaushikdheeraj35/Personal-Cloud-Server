## Web-controlled LED

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode (GPIO.BOARD)

LED_PIN = 7

GPIO.setup(LED_PIN,GPIO.OUT)


pubnub = Pubnub(publish_key='pub-c-2feb27d6-3859-4a13-9445-d06b03e406ee',
                subscribe_key='sub-c-636e0cde-ea8f-11e5-871f-0619f8945a4f')

channel = 'disco'

def _callback(m, channel):
	print(m)
	if m['led'] == 1:
		for i in range(6):
		    GPIO.output(LED_PIN,True)
		    time.sleep(0.5)
		    GPIO.output(LED_PIN,False)
		    time.sleep(0.5)
		    print('blink')

def _error(m):
	print(m)
 
pubnub.subscribe(channels=channel, callback=_callback, error=_error)

