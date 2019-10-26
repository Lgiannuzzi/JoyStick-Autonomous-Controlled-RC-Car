int pin_x = A0;             //set the x direction position read from digital pin A0 
int position_x = 0;     //set a int value can record x position 
int pin_y = A1;
int position_y = 0;
int pin_button= 2;
void setup()
{ 
     
  Serial.begin(9600);   // initialize serial communications at 9600 bps    
  pinMode(pin_x, INPUT);  // set pin mod as INPUT    
  pinMode(pin_y, INPUT);
  pinMode(pin_button, INPUT);
  digitalWrite(pin_button, HIGH);
  Serial.begin(9600);
  
  }
  void read()
  {    position_x = analogRead(pin_x);//digital read from pin_x
       position_y = analogRead(pin_y);     
  }
  void show()
  {
    Serial.print(" X: ");//print information to Serial Monitor 
    Serial.print(position_x);
    Serial.print(", Y:");
    Serial.print(position_y);
    Serial.print("  Button ");
    Serial.print(digitalRead(pin_button));
    Serial.print('\n');
  }
  void loop(){
    read();
    show();
    delay(100); // add some delay between reads (0.1 second delay)   
    }

