#include <LCD_I2C.h>  
LCD_I2C lcd(0x27, 16, 2);   
void setup()  
{  
  lcd.begin();   
  lcd.backlight();  
}  
void loop()  
{  
  lcd.print(" Hello");   
  lcd.setCursor(5, 1);   
  lcd.print("World!");  
  delay(500);  
  for (int i = 0; i < 5; ++i)  
  {  
    lcd.backlight();  
    delay(100); 
    lcd.noBacklight();  
    delay(0);  
  }  
  lcd.backlight();  
  lcd.clear();  
  delay(500);  
}

//SCL = A5
//SDA = A4
