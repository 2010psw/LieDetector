#include "HeartSpeed.h"

HeartSpeed heartspeed(A1);                  ///<The serial port for at observe pulse.

void mycb(uint8_t rawData, int value)
{
  if(rawData){
    Serial.println(value);
  }else{
    Serial.print("HeartRate Value = "); Serial.println(value);
  }
}
void setup() {
  Serial.begin(115200);
  heartspeed.setCB(mycb);    ///Callback function.
  heartspeed.begin();///The pulse test.
}

void loop() {

}
