int ledPin=13;
int sensorPin=0;

void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int value=analogRead(sensorPin);
  Serial.print(value);
  Serial.println(value);

  if (value < 300){
    digitalWrite(13, LOW);
  }
  else {
    digitalWrite(13, HIGH);
  }
}
