#include <IRremote.h>

IRrecv recv(6);
void setup() {
  // put your setup code here, to run once:
  recv.enableIRIn();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (recv.decode()) {
    if(recv.decodedIRData.decodedRawData == 0xF906FF00){
      Serial.println("Ok");
    }
    if(recv.decodedIRData.decodedRawData == 0xE51AFF00){
      Serial.println("Volume Up");
    }
    if(recv.decodedIRData.decodedRawData == 0xB748FF00){
      Serial.println("Volume Down");
    }
    if(recv.decodedIRData.decodedRawData == 0xE817FF00){
      Serial.println("Pause");
    }
    if(recv.decodedIRData.decodedRawData == 0xF807FF00){
      Serial.println("Next");
    }
    if(recv.decodedIRData.decodedRawData == 0xB847FF00){
      Serial.println("prev");
    }
    delay(50);
    recv.resume();
  }

}
