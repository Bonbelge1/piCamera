from picamera import PiCamera
from time import sleep, gmtime, strftime
from gpiozero import LED
from gpiozero import Button
#from RPi.GPIO as GPIO
import os

def pictureName():
        return strftime("%x %H:%M:%S", gmtime())

def videoCapture():
        camera = PiCamera()
        camera.start_recording('/home/pi/Desktop/video.h264')
        sleep(5)

def directory(nb):
        return '/home/pi/Desktop/images/image' + pictureName() + '.jpg'

def main():
        #Create directories for imagese and videos
        if not os.path.exists('/home/pi/Documents/images'):
                os.makedirs('/home/pi/Documents/images')
        if not os.path.exists('/home/pi/Documents/videos'):
                os.makedirs('/home/pi/Documents/videos')
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        #GPIO.setup(27, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        

        ledCam = LED(17)
        ledVid = LED(27)
        buttonCam = Button(2)
        buttonVid = Button(3)

        while True:
                if (buttonCam.buttonPressed(button.UP)):
                        print('camera button pressed')
                        ledCam.on()
                        sleep(2)
                        ledCam.off()
                if (buttonVid.buttonPressed(button.UP)):
                        print('video button pressed')
                        ledVid.on()
                        sleep(2)
                        ledVid.off()          
                
if __name__ == '__main__':
        main()



