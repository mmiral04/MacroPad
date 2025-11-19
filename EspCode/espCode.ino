#include "BluetoothSerial.h"
#include "esp_task_wdt.h"
#include "esp_err.h"


#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif


void print_wakeup_reason() {
  esp_sleep_wakeup_cause_t wakeup_reason;

  wakeup_reason = esp_sleep_get_wakeup_cause();

  switch (wakeup_reason) {
    case ESP_SLEEP_WAKEUP_EXT0:     Serial.println("Wakeup caused by external signal using RTC_IO"); break;
    case ESP_SLEEP_WAKEUP_EXT1:     Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_TIMER:    Serial.println("Wakeup caused by timer"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD: Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP:      Serial.println("Wakeup caused by ULP program"); break;
    default:                        Serial.printf("Wakeup was not caused by deep sleep: %d\n", wakeup_reason); break;
  }
}

String msg;
RTC_DATA_ATTR BluetoothSerial SerialBT;

// Pin numbers
#define N_BUTTONS 9
const int button_pin[N_BUTTONS] = {23, 22, 21, 33, 32, 25, 14, 26, 12};
const int disconnect_pin = 15;
const int led_pin = 13;

bool disconnect_flag;

void connectionProtocol(){
   bool connected = false;
   int state = LOW;
   while (!connected){
      digitalWrite(led_pin, (state == LOW ? HIGH : LOW));
      state = (state == LOW ? HIGH : LOW);
      if (SerialBT.available()){
         msg = "";
         readSerialPort();
         if (msg == "begin connection"){
            SerialBT.print("accept connection");
            SerialBT.flush();
            connected = true;
            Serial.println("Connection stablished");
            digitalWrite(led_pin, LOW);
         }
      }
      delay(1000);
   }
}

void disconnect(){
   digitalWrite(led_pin, HIGH);
   delay(2000);
   digitalWrite(led_pin, LOW);
   esp_light_sleep_start();
   print_wakeup_reason();
   digitalWrite(led_pin, HIGH);
   delay(2000);
   digitalWrite(led_pin, LOW);

}


void checkDisconnect() {
   msg = "";
   readSerialPort();
   if (msg == "disconnected"){
         disconnect_flag = true;
         Serial.println("Disconnected");
         disconnect();
   }
}



void setup() {
   disconnect_flag = false;

   Serial.begin(115200);
   SerialBT.begin("MacroPad"); //Bluetooth device name
   Serial.println("MacroPad device started, now you can pair it!");

   // initialize pins
   for (int i = 0; i < N_BUTTONS; i++){
      pinMode(button_pin[i], INPUT_PULLDOWN);
   }

   pinMode(disconnect_pin, INPUT_PULLDOWN);

   pinMode(led_pin, OUTPUT);

   esp_sleep_enable_ext0_wakeup(GPIO_NUM_15, 1);
   connectionProtocol();
}



void loop(){
   if (disconnect_flag) {
      ESP.restart();
   }

   // read buttons
   int button_state;
   int count = 0;
   for (int i = 0; i < N_BUTTONS; i++){
      button_state = digitalRead(button_pin[i]);
      if (button_state == HIGH){
         char strBuf[7];
         sprintf(strBuf, "Boton %d", i + 1);
         SerialBT.print(strBuf);
         Serial.println(strBuf);
         SerialBT.flush();
         delay(200);
         break;
      }
   }

   button_state = digitalRead(disconnect_pin);
   if (button_state == HIGH) {
      SerialBT.print("disconnect");
      SerialBT.flush();
      Serial.println("Disconnect pressed");
      disconnect();
      ESP.restart();
   }


   checkDisconnect();
}

void readSerialPort(){
   while (SerialBT.available()) {
      delay(10); 
      if (SerialBT.available() > 0) {
            char c = SerialBT.read();  //gets one byte from serial buffer
            msg += c; //makes the string readString
      }
   }
   SerialBT.flush();
}
