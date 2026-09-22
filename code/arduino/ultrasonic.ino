// Standalone ultrasonic test sketch. Change pins for your build.
const byte TRIG=11,ECHO=12;
void setup(){Serial.begin(115200);pinMode(TRIG,OUTPUT);pinMode(ECHO,INPUT);}
void loop(){
 digitalWrite(TRIG,LOW);delayMicroseconds(2);
 digitalWrite(TRIG,HIGH);delayMicroseconds(10);digitalWrite(TRIG,LOW);
 unsigned long d=pulseIn(ECHO,HIGH,30000);
 Serial.println(d?d*.0343/2:999);
 delay(100);
}
