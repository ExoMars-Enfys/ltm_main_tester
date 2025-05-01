#include <Arduino.h>

// code taken from: https://www.pjrc.com/teensy/td_uart.html

// set this to the hardware serial port you wish to use
#define HWSERIAL Serial1

void setup()
{
  Serial.begin(115200);
  HWSERIAL.begin(115200);
}

void loop()
{
  int incomingByte;

  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    Serial.print("USB received: ");
    Serial.println(incomingByte, DEC);
    HWSERIAL.println(incomingByte, DEC);
  }
  if (HWSERIAL.available() > 0)
  {
    incomingByte = HWSERIAL.read();
    Serial.print("UART received: ");
    Serial.println(incomingByte, DEC);
    HWSERIAL.println(incomingByte, DEC);
  }
}