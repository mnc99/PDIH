// C++ code
//

int pin = 0;

void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  for(pin = 13; pin >= 10; pin--){
    digitalWrite(pin, HIGH);
    delay(50);
    digitalWrite(pin, LOW);
  }
  
  for(pin = 10; pin <= 13; pin++){
    digitalWrite(pin, HIGH);
    delay(50);
    digitalWrite(pin, LOW);
  }
}
