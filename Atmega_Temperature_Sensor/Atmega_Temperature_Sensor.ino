#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    delay(10); // hang out until serial port opens
  }
}

void loop() {
  Adafruit_AM2320 am2320 = Adafruit_AM2320();
  am2320.begin();
  while(1){
    Serial.write((int)am2320.readTemperature());
  
    delay(500);
  }
}
