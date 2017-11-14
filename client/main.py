import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.getmode()

# GPIO.setup(17,GPIO.OUT)
# GPIO.setup(18,GPIO.IN)
# GPIO.setup(19,GPIO.OUT)

chan_list = [17,18,19]

GPIO.setup(chan_list,GPIO.OUT)
# GPIO.list_co()
GPIO.output(17,1)
GPIO.output(19,GPIO.HIGH)
