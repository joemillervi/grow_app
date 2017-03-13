import picamera
import time
import datetime
import os

camera = picamera.PiCamera()

# take an image every hour 
def take_image_and_write_file():
	image_title = '/home/pi/grow_app/data/images/{timestamp}.jpg'.format(timestamp=time.time()) 
	camera.capture(image_title)

def find_path_of_most_recent_image():
    image_filenames = os.listdir('/home/pi/grow_app/data/images') 
    image_timestamps = [float(image_filename[:-4]) for image_filename in image_filenames]
    image_timestamps.sort()
    return '/images/' + str(image_timestamps[len(image_timestamps) - 1]) + '.jpg'


