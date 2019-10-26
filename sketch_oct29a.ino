#include<SPI.h>
#include<RF24.h>
int pin_x = A0;             //set the x direction position read from digital pin A0 
int position_x = 0;     //set a int value can record x position 
int pin_y = A1;
int position_y = 0;
int pin_button= 2;
RF24 radio(9, 10);
void setup(void){
  
  Serial.begin(9600);   // initialize serial communications at 9600 bps    
  pinMode(pin_x, INPUT);  // set pin mod as INPUT    
  pinMode(pin_y, INPUT);
  pinMode(pin_button, INPUT);
  digitalWrite(pin_button, HIGH);
  Serial.begin(9600);

  
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x77);       //make sure the channel is same in your raspberry pi
  radio.openWritingPipe(0xF0F0F0F0E1LL);     //make sure the address is same in your raspberry pi
  radio.enableDynamicPayloads();
  radio.powerUp();
}
void read()
{
  position_x = analogRead(pin_x);
  position_y = analogRead(pin_y);
  
}


void loop(void){
  

    const char text[] = "Hello World is awesome";
  radio.write(&text, sizeof(text));
  delay(1000);
}

