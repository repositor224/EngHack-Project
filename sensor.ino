#include <Wire.h>
#include "Adafruit_VCNL4010.h"
#include "LiquidCrystal.h"

const int TMP_PIN = A0;
const int BUTTON_PIN = 2;
const int LED_PIN = 8;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 6;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Adafruit_VCNL4010 vcnl;

void setup() {
  Serial.begin(9600);

  if (! vcnl.begin()){
    Serial.println("Sensor not found :(");
    while (1);
  }

  pinMode(BUTTON_PIN, INPUT_PULLUP);

  pinMode(LED_PIN, OUTPUT);

  lcd.begin(16, 2);
  lcd.print("hello, world!");
}


void loop() {
  // int raw_temp = analogRead(TMP_PIN);
  int raw_light = vcnl.readAmbient();

  // Serial.print("Ambient(light): "); Serial.println(raw_light);

  // double temp = (double)raw_temp / 1024; //find percentage of input reading
  // temp = temp * 5; //multiply by 5V to get voltage
  // temp = temp - 0.5; //Subtract the offset
  // temp = temp * 100; //Convert to degrees

  // Serial.print("Temp: ");
  // Serial.print(temp);
  // Serial.println(" C");

  int button = digitalRead(2);
  // Serial.println("Push button: ");
  // Serial.println(button);

  digitalWrite(LED_PIN, button);
  delay(3000);
  // digitalWrite(LED_PIN, HIGH);
  // delay(500);

  /// LCD 
  lcd.setCursor(0, 1);
  lcd.print(millis() / 1000);

  // communication 
  Serial.print("{\"button\":");
  Serial.print(button);
  Serial.print(",\"light\":");
  Serial.print(raw_light);
  // Serial.print(",\"temp\":");
  // Serial.print(raw_temp);
  Serial.println("}");
}