int IRSensor = 7;
void setup()
{
  pinMode (IRSensor, INPUT); // sensor pin INPUT
  Serial.begin (9600); // Starts the serial communication
}
void loop()
{
  //Define a variables for read the IRsensor
  int Sensordata = digitalRead (IRSensor);
  if (Sensordata == LOW)
  {
    Serial.print(digitalRead (IRSensor));
    Serial.print("\nStop something is ahed");
    Serial.println();
  }
  else
  {
    Serial.print("Path is clear");
    Serial.println();
  }
  delay(2000);
}
