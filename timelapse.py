from picamera import PiCamera
from os import system

#camera.rotation = 180
camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(10):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(5)

system('convert -delay 10 -loop 0 image*.jpg animation.gif')