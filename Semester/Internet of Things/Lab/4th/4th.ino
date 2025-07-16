//void setup()
//{
//  pinMode(2, INPUT);
//  pinMode(7, OUTPUT);
//  Serial.begin(9600);
//}
//void loop()
//{
//  int resistance = digitalRead(7);
//  if(resistance == HIGH){
//    Serial.println("It is dark , LED is turned ON");
//    digitalWrite(7,HIGH);
//  }
//  else
//  {
//    Serial.println("It is day time , LED is turned OFF");
//    digitalWrite(7,LOW);
//  }
//  delay(500);
//}


void setup() {
  pinMode(2, INPUT);  // LDR sensor input
  pinMode(7, OUTPUT); // LED output
  Serial.begin(9600);
}

void loop() {
  int light = digitalRead(2); // Read LDR sensor value

  if (light == HIGH) { // Assuming LOW = dark
    Serial.println("It is dark, LED is ON");
    digitalWrite(7, HIGH);
  } else {
    Serial.println("It is bright, LED is OFF");
    digitalWrite(7, LOW);
  }
  
  delay(500);
}
