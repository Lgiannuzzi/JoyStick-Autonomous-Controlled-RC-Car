from gpiozero import PWMOutputDevice
import time

PWM_DRIVE_LEFT = 21
FORWARD_LEFT_PIN = 2
REVERSE_LEFT_PIN = 3

PWM_DRIVE_RIGHT = 20
FORWARD_RIGHT_PIN = 14
REVERSE_RIGHT_PIN = 15


driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True,0 ,1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True,0 ,1000)

forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN, True,0 ,1000)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN, True,0 ,1000)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN, True,0 ,1000)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN, True,0 ,1000)

def stop():
    forwardLeft.value = False
    reverseLeft.value = False
    forwardRight.value = False
    reverseRight.value = False
    driveLeft.value = 0
    driveRight.value = 0
    
    
def go():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    '''
    driveLeft.value = 1.0
    driveRight.value = 1.0
    '''
    
def reverse():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0
    
def spinleft():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0
    
def spinright():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = 1.0
    driveRight.value = 1.0
    
def forwardleft():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = .2
    driveRight.value = .8    
    
def forwardright():
    forwardLeft.value = True
    reverseLeft.value = False
    forwardRight.value = True
    reverseRight.value = False
    driveLeft.value = .8
    driveRight.value = .2
    
def reverseleft():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = .8
    driveRight.value = .2   
  
def reverseleft():
    forwardLeft.value = False
    reverseLeft.value = True
    forwardRight.value = False
    reverseRight.value = True
    driveLeft.value = .2
    driveRight.value = .8 
    
    
    
if __name__== '__main__':
    
    while 1:
        stop()
        
        driveLeft.value = 1
        driveRight.value = 1
        go()
        time.sleep(2)
        stop()
        driveLeft.value = .8
        driveRight.value = .8
        go()
        time.sleep(2)
        
        stop()
        driveLeft.value = 1
        driveRight.value = 1
        reverse()
        time.sleep(2)
        stop()
        driveLeft.value = .8
        driveRight.value = .8
        reverse()
        time.sleep(2)  
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    

