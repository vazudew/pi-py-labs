import RPi.GPIO as GPIO
import time
from threading import Thread

# new comment
pin1=18
pin2=23

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pin1,GPIO.OUT)
	GPIO.setup(pin2,GPIO.OUT)

def pinOn(pin):
	print "LED on :" + str(pin)
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(2)


def pinOff(pin):
	print "LED off"
	GPIO.output(pin,GPIO.LOW)
	time.sleep(5)

def glow(pin, threadid):
	for i in range(5):
		pinOn(pin)
		pinOff(pin)

setup()

try :
	t1 = Thread(target=glow,args=(pin1,1))
	t1.start()
	t2 = Thread(target=glow,args=(pin2,0))
	t2.start()
except Exception as e:
	print "error with threads"
	print str(e)

