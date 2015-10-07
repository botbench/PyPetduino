#include <LedControl.h>
#include <Petduino.h>

#include <CmdMessenger.h>
#include <PetduinoSerial.h>

PetduinoSerial pet = PetduinoSerial();

byte X[8]={
  B10000001,
  B01000010,
  B00100100,
  B00011000,
  B00100100,
  B01000010,
  B10000001,
  B00000000
};

void setup() {

  // Setup Petduino
//  Serial.println("Starting...");
  pet.begin(9600); // Serial baud rate
  pet.setOnDataCallback(onData);

}

void loop() 
{
  // Update pet
  pet.update();

  // Do your thing...
}

void onData(char *data) {
  char *pos = data;
  byte val[8];
  int count = 0;

  // Need 16 characters in total
  if (strlen(data) != 16)
  {
//    char buff[32];
//    Serial.print("Malformed data: ");
//    sprintf(buff, "size: %d", strlen(data));
//    Serial.println(buff);
    pet.drawImage(X);
    return;
  }
    
   /* WARNING: no sanitization or error-checking whatsoever */
  for(count = 0; count < sizeof(val)/sizeof(val[0]); count++) {
      sscanf(pos, "%2hhx", &val[count]);
      pos += 2;
  }

//  Serial.println(data);
  pet.drawImage(val);
}
