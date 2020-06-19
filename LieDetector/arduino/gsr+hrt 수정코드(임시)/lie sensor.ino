
#include "HeartSpeed.h"

HeartSpeed heartspeed(A1);

const int GSR=A2;
int sensorValue=0;
int gsr_average=0;


 void mycb(uint8_t rawData, int value)
{
  if(rawData){
    Serial.println(value);
  }else{
    Serial.print("hrt="); Serial.println(value);
  }
}


void setup(){
  Serial.begin(9600);

  heartspeed.setCB(mycb);    ///Callback function.
  heartspeed.begin();///The pulse test.
  }

void loop(){
  int sum=0;
  for(int i=0;i<10;i++)
  {
    sensorValue=analogRead(GSR);
    sum += sensorValue;
    delay(5);
  }
  gsr_average = sum/10;
  Serial.println(gsr_average);
}
   
