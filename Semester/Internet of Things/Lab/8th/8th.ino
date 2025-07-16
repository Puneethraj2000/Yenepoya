int smoke=A3;
void setup()
{
  Serial.begin(9600);
  pinMode(A3,INPUT);
  pinMode(2,OUTPUT);
}
void loop()
{
  int ss=analogRead(A3);
  Serial.println("smoke value is");
  Serial.println(ss);
  if(ss>400)
  digitalWrite(2,HIGH);
  else
  digitalWrite(2,LOW);
  delay(2000);
}
