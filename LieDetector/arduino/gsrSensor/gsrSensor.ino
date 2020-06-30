
#include "HeartSpeed.h"

HeartSpeed heartspeed(A1);

const int BUZZER=3; //버저를 지우면 소스는 돌아가나 내부 웹에서 그래프 수치값이 
const int GSR=A2;
int threshold=0;
int gsr;


 void mycb(uint8_t rawData, int value)
{
  if(rawData){
    Serial.println(value);
  }else{
    Serial.print("hrt = "); Serial.println(value);
  }
}


void setup(){
  long sum=0;
  Serial.begin(9600);
  pinMode(BUZZER,OUTPUT);
  digitalWrite(BUZZER,LOW);
  delay(2000);

  heartspeed.setCB(mycb);    ///Callback function.
  heartspeed.begin();///The pulse test.
  
  
  for(int i=0;i<500;i++)
  {
  gsr=analogRead(GSR);
  sum += gsr;
  delay(5);
  }
  threshold = sum/500;
   Serial.print("");
   Serial.println(threshold);
  }

void loop(){
  int temp;
  gsr=analogRead(GSR);
  Serial.print("gsr = ");
  Serial.println(gsr);
  temp = threshold - gsr;
  if(abs(temp)>50)
  {
    gsr=analogRead(GSR);
    temp = threshold - gsr;
    if(abs(temp)>50){
    digitalWrite(BUZZER,HIGH);
    //Serial.println("YES!");
    delay(2000);
    digitalWrite(BUZZER,LOW);
    delay(1000);}
  }
  }
