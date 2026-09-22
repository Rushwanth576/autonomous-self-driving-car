Wiring
L298N → Arduino UNO
ENA → D5; IN1 → D7; IN2 → D8; ENB → D6; IN3 → D9; IN4 → D10.
Sensors → Arduino UNO
Left IR OUT → A0; Right IR OUT → A1; Ultrasonic TRIG → D11; Ultrasonic ECHO → D12.
Raspberry Pi
Camera → CSI connector. Arduino UNO → USB. Serial → 115200 baud.
Motors
Two left motors are connected to one L298N bridge; two right motors to the other bridge. Reverse a motor pair's polarity if its direction is opposite.
Power
Use a suitable regulated Raspberry Pi supply and an appropriate motor supply. Do not power motors from the Raspberry Pi 5V rail. Verify actual motor/driver current ratings before operation.
