/*
  Autonomous Self-Driving Car
  Arduino UNO Motor + Sensor Controller

  L298N:
  ENA -> D5
  IN1 -> D7
  IN2 -> D8
  ENB -> D6
  IN3 -> D9
  IN4 -> D10

  Ultrasonic:
  TRIG -> D11
  ECHO -> D12

  IR sensors:
  Left  -> A0
  Right -> A1

  Serial commands:
  L120,R120
  S
*/

const byte LEFT_EN  = 5;
const byte LEFT_IN1 = 7;
const byte LEFT_IN2 = 8;

const byte RIGHT_EN  = 6;
const byte RIGHT_IN1 = 9;
const byte RIGHT_IN2 = 10;

const byte TRIG_PIN = 11;
const byte ECHO_PIN = 12;

const byte IR_LEFT_PIN  = A0;
const byte IR_RIGHT_PIN = A1;

String buffer;

void setup() {
  pinMode(LEFT_EN, OUTPUT);
  pinMode(LEFT_IN1, OUTPUT);
  pinMode(LEFT_IN2, OUTPUT);

  pinMode(RIGHT_EN, OUTPUT);
  pinMode(RIGHT_IN1, OUTPUT);
  pinMode(RIGHT_IN2, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(IR_LEFT_PIN, INPUT);
  pinMode(IR_RIGHT_PIN, INPUT);

  Serial.begin(115200);
  stopMotors();
}

void setMotor(byte en, byte in1, byte in2, int speedValue) {
  speedValue = constrain(speedValue, -255, 255);

  if (speedValue > 0) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(en, speedValue);
  }
  else if (speedValue < 0) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(en, -speedValue);
  }
  else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    analogWrite(en, 0);
  }
}

void stopMotors() {
  setMotor(LEFT_EN, LEFT_IN1, LEFT_IN2, 0);
  setMotor(RIGHT_EN, RIGHT_IN1, RIGHT_IN2, 0);
}

float distanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return 999.0;
  }

  return duration * 0.0343 / 2.0;
}

void sendSensors() {
  int irLeft = digitalRead(IR_LEFT_PIN);
  int irRight = digitalRead(IR_RIGHT_PIN);
  float distance = distanceCM();

  Serial.print("I0");
  Serial.print(irLeft);

  Serial.print(",I1");
  Serial.print(irRight);

  Serial.print(",D");
  Serial.println(distance, 1);
}

void parseDrive(String command) {
  int comma = command.indexOf(",R");

  if (!command.startsWith("L") || comma < 0) {
    stopMotors();
    return;
  }

  int left = command.substring(1, comma).toInt();
  int right = command.substring(comma + 2).toInt();

  left = constrain(left, -255, 255);
  right = constrain(right, -255, 255);

  setMotor(LEFT_EN, LEFT_IN1, LEFT_IN2, left);
  setMotor(RIGHT_EN, RIGHT_IN1, RIGHT_IN2, right);
}

void processCommand(String command) {
  command.trim();

  if (command == "S") {
    sendSensors();
  }
  else if (command.startsWith("L")) {
    parseDrive(command);
  }
  else {
    stopMotors();
  }
}

void loop() {
  while (Serial.available() > 0) {
    char c = Serial.read();

    if (c == '\n') {
      processCommand(buffer);
      buffer = "";
    }
    else if (c != '\r' && buffer.length() < 40) {
      buffer += c;
    }
    else if (buffer.length() >= 40) {
      buffer = "";
      stopMotors();
    }
  }
}
