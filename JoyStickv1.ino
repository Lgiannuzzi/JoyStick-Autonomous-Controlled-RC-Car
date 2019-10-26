#include <nRF24L01.h>
#include <printf.h>
#include <RF24.h>
#include <RF24_config.h>
#include<SPI.h>

// ce, csn pins
RF24 radio(9, 10);
int pin_x = A0;     //set the x direction position read from digital pin A0
int pin_y = A1; 
int sw = A2; 
int position_x = 0;
int position_y = 0; 
int sw_press = 0; 


void setup(void){
  Serial.begin(9600);       // initialize serial communications at 9600 bps
  pinMode(pin_x, INPUT);
  pinMode(pin_y,INPUT); // set pin mode as INPUT
  pinMode(sw,INPUT);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x70);       //make sure the channel is same in your raspberry pi
  radio.openWritingPipe(0xF0F0F0F0E1LL);     //make sure the address is same in your raspberry pi
  radio.enableDynamicPayloads();
  radio.powerUp();
}

void read()
{
  position_x = analogRead(pin_x);   //digital read from pin_x
  position_y = analogRead(pin_y);  
  sw_press = analogRead(sw); 
  
}

void loop(void)
{
  read();
    

  if(position_x >509 && position_x <514 && position_y >516 && position_y <521)
  {
    const char text[] = "Stop";
    radio.write(&text,sizeof(text)); 
    Serial.println("f");
  }
    
  if(position_x >525) 
  {
    const char text[] = "Forward";
    radio.write(&text,sizeof(text)); 
    Serial.println("w");
  }
  if(position_x<500) 
  {
    const char text[] = "Backward";
    radio.write(&text,sizeof(text)); 
    Serial.println("s");
  }
  if((position_y>525)&&(position_x>500))
  {
    const char text[] = "Right";
    radio.write(&text,sizeof(text)); 
    Serial.println("d");
  }
  if((position_y<500)&&(position_x>500))
  {
    const char text[] = "Left";
    radio.write(&text,sizeof(text)); 
    Serial.println("a");
  }
   if(sw_press ==0) 
  {
    const char text[] = "Stop";
    radio.write(&text,sizeof(text)); 
    Serial.println("f");
  }
  delay(100);
 }
 
 
