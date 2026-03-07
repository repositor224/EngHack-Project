#include <Wire.h>
#include "Adafruit_VCNL4010.h"
#include "LiquidCrystal.h"
#include "Servo.h"
#include "ArduinoJson.h"

const int TMP_PIN = A0;
const int BUTTON_PIN = 2;
const int SERVO_PIN = 7;
const int LED_PIN = 8;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 6;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Adafruit_VCNL4010 vcnl;
Servo servo;

int servo_pos = 90;
bool servo_on = false; //rotation on/off

bool last_button_state = LOW;

void setup() {
  Serial.begin(9600);

  if (! vcnl.begin()){
    Serial.println("Sensor not found :(");
    while (1);
  }


  pinMode(BUTTON_PIN, INPUT_PULLDOWN);
  pinMode(LED_PIN, OUTPUT);

  lcd.begin(16, 2);
  lcd.print("hello, world!");

  servo.attach(SERVO_PIN);
}


void loop() {
  int raw_light = vcnl.readAmbient();
  int raw_temp = analogRead(TMP_PIN);
  int temp = getTempC(raw_temp);

  serialWrite(raw_light, temp);

  buttonToggle();
  // Serial.println("Push button: ");
  // Serial.println(button);
  // digitalWrite(LED_PIN, button);

  /// LCD 
  lcd.setCursor(0, 1);
  lcd.print(millis() / 1000);

  // rotate();

  serialRead();

  delay(500);
}

void rotate() {
    for (servo_pos = 0; servo_pos <= 180; servo_pos += 1) {
      servo.write(servo_pos);
      delay(100);
    }
    for (servo_pos = 180; servo_pos >= 0; servo_pos -= 1) {
      servo.write(servo_pos);
      delay(100);
    }
}

// {light" #, temperature: #}
void serialWrite(int light, int temp) {
  Serial.print("{\"light\":");
  Serial.print(light);
  Serial.print(",\"temperature\":");
  Serial.print(temp);
  Serial.println("}");
}

void serialRead() {
  if (Serial.available()) {

    String msg = Serial.readStringUntil('\n');

    StaticJsonDocument<512> doc;

    DeserializationError err = deserializeJson(doc, msg);

    if (err) {
      Serial.println("JSON parse failed");
      return;
    }

    const char* advice = doc["ai_advice"];

    displayMsg(advice);
  }
}

int getTempC(int raw) {
  double temp = (double)raw / 1024; //find percentage of input reading
  temp = temp * 5; //multiply by 5V to get voltage
  temp = temp - 0.5; //Subtract the offset
  temp = temp * 100; //Convert to degrees

  // Serial.print("Temp: ");
  // Serial.print(temp);
  // Serial.println(" C");

  return temp;
}

void buttonToggle() {
  bool button_state = digitalRead(BUTTON_PIN);

  if (last_button_state == LOW && button_state == HIGH) {
    servo_on = !servo_on;
    delay(20);
  }

  last_button_state = button_state;
}

void displayMsg(String msg) {

  lcd.clear();
  lcd.begin(16, 2);
  lcd.print(msg);

  int len = msg.length();
}