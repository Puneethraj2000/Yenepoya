int led = 12; 
int brightness = 0;   
int fadeAmount = 5;   
void setup()  
{  
pinMode(led, OUTPUT);  
}  
void loop()  
{  
analogWrite(led, brightness);  
brightness = brightness + fadeAmount; 
if (brightness <= 0 || brightness >= 255)  
{  
fadeAmount = -fadeAmount;  
}  
delay(20);  
} 
