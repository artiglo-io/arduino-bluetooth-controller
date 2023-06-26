#include <SoftwareSerial.h>
#include <AFMotor.h>

SoftwareSerial BT(9, 10);

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

char command;
const int motorSpeed = 255;
unsigned long previousMillis = 0;
const unsigned int timeout = 300;

void setup() {
    Serial.begin(9600);
    BT.begin(9600);
}

void loop() {
    if (BT.available()) {
        command = BT.read();
        previousMillis = millis();
        switch (command) {
            case '1':
                forward();
                break;
            case '2':
                left();
                break;
            case '3':
                stop();
                break;
            case '4':
                right();
                break;
            case '5':
                backward();
                break;
        }
    } else {
        if (millis() - previousMillis > timeout) {
            stop();
        }
    }
}

void forward(){
    motor1.run(FORWARD);
    motor2.run(FORWARD);
    motor3.run(FORWARD);
    motor4.run(FORWARD);
    motor1.setSpeed(motorSpeed/2);
    motor2.setSpeed(motorSpeed/2);
    motor3.setSpeed(motorSpeed/2);
    motor4.setSpeed(motorSpeed/2);
}

void backward(){
    motor1.run(BACKWARD);
    motor2.run(BACKWARD);
    motor3.run(BACKWARD);
    motor4.run(BACKWARD);
    motor1.setSpeed(motorSpeed/2);
    motor2.setSpeed(motorSpeed/2);
    motor3.setSpeed(motorSpeed/2);
    motor4.setSpeed(motorSpeed/2);
}

void left(){
    motor2.run(FORWARD);
    motor3.run(FORWARD);
    motor1.setSpeed(0);
    motor2.setSpeed(motorSpeed);
    motor3.setSpeed(motorSpeed);
    motor4.setSpeed(0);
}

void stop(){
    motor1.setSpeed(0);
    motor2.setSpeed(0);
    motor3.setSpeed(0);
    motor4.setSpeed(0);
}

void right(){
    motor1.run(FORWARD);
    motor4.run(FORWARD);
    motor1.setSpeed(motorSpeed);
    motor2.setSpeed(0);
    motor3.setSpeed(0);
    motor4.setSpeed(motorSpeed);
}
