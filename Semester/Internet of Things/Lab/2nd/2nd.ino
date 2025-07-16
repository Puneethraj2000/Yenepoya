//#include <DHT.h> // Include library
//#define outPin 8 // Defines pin number to which the sensor is connected
//DHT dht; // Creates a DHT object
//void setup()
//{
//Serial.begin(9600); // initialize serial communication at 9600 bits per second
//}
//void loop()
//{
//int readData = dht.read11(outPin);
//float t = dht.temperature; // Read temperature
//float h = dht.humidity; // Read humidity
//Serial.print("Temperature = ");
//Serial.print(t);
//Serial.print("°C | ");
//Serial.print((t*9.0)/5.0+32.0); // Convert celsius to fahrenheit
//Serial.println("°F ");
//Serial.print("Humidity = ");
//Serial.print(h);
//Serial.println("% ");
//Serial.println("");
//delay(2000); // wait two seconds
//}


//#include <DHT.h>  // Include the DHT library
//
//#define DHTPIN 8      // Defines the pin number to which the sensor is connected
//#define DHTTYPE DHT11 // Define the sensor type (DHT11, DHT22, or DHT21)
//
//// Create a DHT object with the correct constructor
//DHT dht(DHTPIN, DHTTYPE);
//
//void setup() {
//  Serial.begin(9600); // Initialize serial communication
//  dht.begin();        // Initialize the DHT sensor
//}
//
//void loop() {
//  float h = dht.readHumidity();       // Read humidity
//  float t = dht.readTemperature();    // Read temperature in Celsius
//
//  // Check if the sensor reading failed
//  if (isnan(h) || isnan(t)) {
//    Serial.println("Failed to read from DHT sensor!");
//    return;
//  }
//
//  Serial.print("Temperature = ");
//  Serial.print(t);
//  Serial.print("°C | ");
//  Serial.print((t * 9.0) / 5.0 + 32.0); // Convert Celsius to Fahrenheit
//  Serial.println("°F ");
//
//  Serial.print("Humidity = ");
//  Serial.print(h);
//  Serial.println("% ");
//  
//  Serial.println(""); // Newline for readability
//
//  delay(2000); // Wait two seconds before next reading
//}



#include <DHT.h>

#define DHTPIN 8      // Sensor connected to pin 8
#define DHTTYPE DHT11 // DHT sensor type

DHT dht(DHTPIN, DHTTYPE); // Create DHT object

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature(); // Read temperature (Celsius)
  float h = dht.readHumidity();    // Read humidity

  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print("°C | ");
  Serial.print(t * 9 / 5 + 32); // Convert to Fahrenheit
  Serial.println("°F");

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.println("%");

  delay(2000); // Wait 2 seconds
}
