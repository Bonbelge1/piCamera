from picamera import PiCamera
from time import sleep, gmtime, strftime, time
from gpiozero import LED, Button
import RPi.GPIO as GPIO
from datetime import datetime
import os

def cameraCapture():
        camera = PiCamera()
        dateString = datetime.now().strftime("%y/%m/%d_%H:%M:%S.%f")
        path = '/home/pi/Documents/images/image_'
        camera.capture(path + dateString +'.jpg')

def timelapse(delay):
        camera = PiCamera()
        for i in range(10):
                camera.capture('image{0:04d}.jpg'.format(i))

        #system('convert -delay 10 -loop 0 image*.jpg animation.gif')
        return True


def videoCapture():
        camera = PiCamera()
        camera.start_recording('/home/pi/Desktop/video.h264')
        sleep(5)

# Create functions to run when the buttons are pressed
def Input_1(channel):
        # Put whatever Button 1 does in here
        print 'Button 1';
            
def Input_2(channel):
        # Put whatever Button 2 does in here
        print 'Button 2';


def main():
        #Create directories for imagese and videos
        if not os.path.exists('/home/pi/Documents/images'):
                os.makedirs('/home/pi/Documents/images')
        if not os.path.exists('/home/pi/Documents/videos'):
                os.makedirs('/home/pi/Documents/videos')        

        #ledCam = LED(17)
        #ledTimelapse = LED(27)
        #buttonCam = Button(2)
        #buttonTimelapse = Button(3)

        GPIO.setmode(GPIO.BCM)
        
        BUTTON_1 = 2           # Sets our input pins
        BUTTON_2 = 3           # Sets our input pins
        LED_1 = 17
        LED_2 = 27
        
        GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LED_1, GPIO.OUT)
        GPIO.setup(LED_2, GPIO.OUT)

        # Wait for Button 1 to be pressed, run the function in "callback" when it does, also software debounce for 300 ms to avoid triggering it multiple times a second
        GPIO.add_event_detect(BUTTON_1, GPIO.BOTH, callback=Input_1, bouncetime=300) 
        GPIO.add_event_detect(BUTTON_2, GPIO.BOTH, callback=Input_2, bouncetime=300) # Wait for Button 2 to be pressed
        
        # Start a loop that never ends
        while True:
                # Put anything you want to loop normally in here
                sleep(60);           # Sleep for a full minute, any interrupt will break this so we are just saving cpu cycles.

        
if __name__ == '__main__':
        main()



