import picamera
import time
import datetime

camera = picamera.PiCamera()

# take an image every hour 
while True:
	image_title = './../data/images/{timestamp}.jpg'.format(timestamp=time.time()) 
	camera.capture(image_title)
	time.sleep(60)
