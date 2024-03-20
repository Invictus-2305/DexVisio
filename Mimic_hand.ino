#include <Servo.h>
Servo myservo1; 
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;

#define SERVO_PIN1 9
#define SERVO_PIN2 10
#define SERVO_PIN3 11
#define SERVO_PIN4 12
#define SERVO_PIN5 13

void setup() {
  myservo1.attach(SERVO_PIN1);
  myservo2.attach(SERVO_PIN2);
  myservo3.attach(SERVO_PIN3);
  myservo4.attach(SERVO_PIN4);
  myservo5.attach(SERVO_PIN5);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();
    if (signal == '1') {
      myservo1.write(180);
    } else if (signal == '0') {
      myservo1.write(0);
    }
    if (signal == '2') {
      myservo2.write(180);
    } else if (signal == '3') {
      myservo2.write(0);
    }
    if (signal == '4') {
      myservo3.write(180);
    } else if (signal == '5') {
      myservo3.write(0);
    }
    if (signal == '6') {
      myservo4.write(180);
    } else if (signal == '7') {
      myservo4.write(0);
    }
    if (signal == '8') {
      myservo5.write(180);
    } else if (signal == '9') {
      myservo5.write(0);
    }
  }
}
