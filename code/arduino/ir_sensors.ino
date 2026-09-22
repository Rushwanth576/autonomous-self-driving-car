// Standalone IR sensor test. Change pins for your modules.
const byte LEFT=A0,RIGHT=A1;
void setup(){Serial.begin(115200);pinMode(LEFT,INPUT);pinMode(RIGHT,INPUT);}
void loop(){
 Serial.print("LEFT=");Serial.print(digitalRead(LEFT));
 Serial.print(" RIGHT=");Serial.println(digitalRead(RIGHT));
 delay(100);
}
