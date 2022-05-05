// C++ code
//

int buttonState = 0;
void setup()
{
  //Pin 13: LED Rojo
  pinMode(13, OUTPUT);
  //Pin 12: LED Amarillo
  pinMode(12, OUTPUT);
  //Pin 11: LED Verde
  pinMode(11, OUTPUT);
  //Pin 7: Pulsador
  pinMode(7, INPUT);
}

void loop()
{
  buttonState = digitalRead(7);
  
  if (buttonState == LOW){
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    delay(1500); // Wait for 1500 millisecond(s)
  
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    delay(1500); // Wait for 1500 millisecond(s)
  
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    delay(1500); // Wait for 1500 millisecond(s)
  }
  else{
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }
  delay(10);
}
