import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.OUT)


#add a feedback

def feedback(channel):
	print "clear feeedbakc"
	GPIO.output(21, GPIO.LOW)
	if GPIO.input(19):
		print "motion detected"
		GPIO.output(21, GPIO.HIGH)
	
GPIO.add_event_detect(19, GPIO.BOTH, callback=feedback, bouncetime=100)
	
try:
	while True:
		sleep(1)


finally:
	GPIO.cleanup()
	print "tilima"
