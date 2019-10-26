import RPi.GPIO as GPIO
from lib_nrf24 import NRF24 # make sure save your program and the changed file on the same directory
import time 
import spidev

#Pin list 
#-----------------------------------
enA = 18
enB = 21
motorF1 = 5
motorF2 = 6
motorB1 = 13
motorB2 = 19 


#Car I/O setup 
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorF1,GPIO.OUT)
GPIO.setup(motorF2,GPIO.OUT)
GPIO.setup(motorB1,GPIO.OUT)
GPIO.setup(motorB2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
motor1Speed = GPIO.PWM(enA,800)
motor2Speed = GPIO.PWM(enB,800)

#Wireless radio/JoyComm setup 
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]  #set your address

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)              #set your CE pin

radio.setPayloadSize(32)
radio.setChannel(0x76)							#set your channel 
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()


print ("Trying stuff")
def speedSetup():
	motor1Speed.start(0)
	motor2Speed.start(0)
	

def back():
	GPIO.output(5,True)
	GPIO.output(6,False)
	GPIO.output(13,True)
	GPIO.output(19,False)
	#GPIO.cleanup() 
	
def go():
    GPIO.output(6,True)
    GPIO.output(5,False)
    GPIO.output(19,True)
    GPIO.output(13,False)

def left():
    GPIO.output(6,True)
    GPIO.output(5,False)
    GPIO.output(13,True)
    GPIO.output(19,False)
   

def right():
    GPIO.output(5,True)
    GPIO.output(6,False)
    GPIO.output(19,True)
    GPIO.output(13,False)

def stop():
    GPIO.output(5,False)
    GPIO.output(6,False)
    GPIO.output(19,False)
    GPIO.output(13,False)
	
def speedControl(Speed1,Speed2):
	motor1Speed.ChangeDutyCycle(Speed1)
	motor2Speed.ChangeDutyCycle(Speed2)

# if __name__== '__main__':
    # command = input ("What you want?: ")

while 1:
	while not radio.available(0):
		time.sleep(1 / 100)
	receivedMessage = []
	radio.read(receivedMessage, radio.getDynamicPayloadSize())
	#print("Received: {}".format(receivedMessage))
	
	time.sleep(1) 
	string = ""
	for n in receivedMessage:
	# Decode into standard unicode set
		if (n >= 32 and n <= 126):
			string += chr(n)
	print(string)		
	command = string
	if command == "w":
		speedSetup()
		go()
		speedControl(70,70)
		#GPIO.cleanup() 
	elif command == 's':
		back()
		speedControl(95,95)
	elif command == 'a':
		speedSetup()
		left()
		speedControl(90,80)
	elif command == 'd':
		speedSetup()
		right()
		speedControl(64,40)
	elif command == 'f':
		stop()
	elif command == 'speed':
		speedControl();
	elif command == 'exit':
		break



GPIO.cleanup() 
