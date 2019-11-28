/*************************************************** 
  This is an example sketch for our optical Fingerprint sensor

  Designed specifically to work with the Adafruit BMP085 Breakout 
  ----> http://www.adafruit.com/products/751

  These displays use TTL Serial to communicate, 2 pins are required to 
  interface
  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/


#include <Adafruit_Fingerprint.h>
#include <LiquidCrystal.h>
#include<SoftwareSerial.h>

#define DEBUG true
unsigned char check_connection=0;
unsigned char times_check=0;
String mySSID = "FOURmidables";       // WiFi SSID
String myPWD = "secondhome"; // WiFi Password
String myAPI = "358ERYUMEQ3PDS0H";   // API Key
String myHOST = "api.thingspeak.com";
String myPORT = "80";
String myFIELD = "field1"; 
int sendVal;

// On Leonardo/Micro or others with hardware serial, use those! #0 is green wire, #1 is white
// uncomment this line:
// #define mySerial Serial1

// For UNO and others without hardware serial, we must use software serial...
// pin #2 is IN from sensor (GREEN wire)
// pin #3 is OUT from arduino  (WHITE wire)
// comment these two lines if using hardware serial
SoftwareSerial mySerial(2, 3);
SoftwareSerial ESP8266(10,11); //wifi
//SoftwareSerial gsm(A2,A3);
LiquidCrystal lcd(12, A5,A4,A3,A2,A1);
String apiKey = "BDCV34ADTQ3VXJNO";
int vb=0,vc=0;

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup()  
{
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  //delay(1000);
  
  lcd.begin(16,2);
  pinMode(13,OUTPUT);
  pinMode(A0,INPUT);
  digitalWrite(13,LOW);
  
   //elay(2000);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);
  Serial.println("\n\nAdafruit finger detect test");

  // set the data rate for the sensor serial port
  finger.begin(57600);
  delay(5);
  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }

  finger.getTemplateCount();
  Serial.print("Sensor contains "); Serial.print(finger.templateCount); Serial.println(" templates");
  Serial.println("Waiting for valid finger...");
}

void loop()                     // run over and over again
{
  
  // Serial.println("inside while");
    getFingerprintIDez();
 // Serial.print("back to loop");
  delay(2000);//don't ned to run this at full speed.
  }
}

uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.println("No finger detected");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }

  // OK success!

  p = finger.image2Tz();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }
  
  // OK converted!
  p = finger.fingerFastSearch();
  if (p == FINGERPRINT_OK) {
    Serial.println("Found a print match!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
    Serial.println("Did not find a match");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }   
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence); 
  //gsm.println("ATD/+917892221826/");
  lcd.print("please vote!");
  lcd.setCursor(0,0);
  while(!digitalRead(A0))
   {
    //Serial.print("some problem in button connection!");
   }
  digitalWrite(13,HIGH);
   delay(3000);
  digitalWrite(13,LOW);

  lcd.print("BJP wins!");
  return finger.fingerID;
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  Serial.print("Waiting for a voter...");
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;
  
  // found a match!
  Serial.print("Found ID no."); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence);
  Serial.println("");
  //gsm.println("ATD+7892221826;");
  //delay(1000);
 lcd.print("please vote!");
  lcd.setCursor(0,0);
  int a,b;
  while(!(a=digitalRead(6))&&!(b=digitalRead(8)) )
   {
   // Serial.print("some problem in button connection!");
   }
   if(a)
   {
    vb++;
    digitalWrite(7,HIGH);
   }
   if(b)
   {
    vc++;
    digitalWrite(7,HIGH);
   }
lcd.clear();
  lcd.print("vote given!");
  delay(2000);
   digitalWrite(7,LOW);
  Serial.println("thanks for voting...sending data to server");
  
   esp(vb,vc);

  return finger.fingerID; 
}
void esp(int sendVal1,int sendVal2)

{   
    ESP8266.begin(115200);
    /*
    espData("AT+RST", 1000, DEBUG);                      //Reset the ESP8266 module
    espData("AT+CWMODE=1", 1000, DEBUG);                 //Set the ESP mode as station mode
    espData("AT+CWJAP=\""+ mySSID +"\",\""+ myPWD +"\"", 1000, DEBUG); 
    //sendVal = random(1000); // Send a random number between 1 and 1000
    String sendData = "GET /update?api_key="+ myAPI +"&"+ myFIELD +"="+String(sendVal1)+"&field2="+String(sendVal2);
    espData("AT+CIPMUX=1", 1000, DEBUG);       //Allow multiple connections
    espData("AT+CIPSTART=0,\"TCP\",\""+ myHOST +"\","+ myPORT, 1000, DEBUG);
    espData("AT+CIPSEND=0," +String(sendData.length()+4),1000,DEBUG);  
    espSerial.find(">"); 
    espSerial.println(sendData);
    Serial.print("Value to be sent: ");
    Serial.println(sendVal1);
    Serial.println(sendVal2);
     
    espData("AT+CIPCLOSE=0",1000,DEBUG);
    delay(10000); 
   espSerial.println("AT+RST");                      //Reset the ESP8266 module
    espSerial.println("AT+CWMODE=1");                 //Set the ESP mode as station mode
//  String a = "AT+CWJAP=\""+mySSID+"\",\""+myPWD+"\"";
    espSerial.println("AT+CWJAP=\""+ mySSID +"\",\""+ myPWD +"\""); 
    //sendVal = random(1000); // Send a random number between 1 and 1000
   String sendData = "GET /update?api_key="+ myAPI +"&"+ myFIELD +"="+String(sendVal1)+"&field2="+String(sendVal2);
    espSerial.println("AT+CIPMUX=0");       //Allow multiple connections
    espSerial.println("AT+CIPSTART=\"TCP\",\""+ myHOST +"\","+ myPORT);
    espSerial.println("AT+CIPSEND=" +String(sendData.length()+4));  
    espSerial.find(">"); 
    espSerial.println(sendData);
    Serial.print("Value to be sent: ");
    Serial.println(sendVal1);
    Serial.println(sendVal2); 
    espSerial.println("AT+CIPCLOSE");
    delay(10000); //
    
  }

  String espData(String command, const int timeout, boolean debug)
{
  Serial.print("AT Command ==> ");
  Serial.print(command);
  Serial.println("     ");
  
  String response = "";
  espSerial.println(command);
  long int time = millis();
  while ( (time + timeout) > millis())
  {
    while (espSerial.available())
    {
      char c = espSerial.read();
      response += c;
    }
  }
  if (debug)
  {
//    Serial.print(response);
  }
  return response;
} */
ESP8266.println("AT+RST");
ESP8266.println("AT+CWMODE=1");
  delay(2000);
  Serial.println("Connecting to Wifi");
   while(check_connection==0)
  {
    Serial.print(".");
 // ESP8266.print("AT+CWJAP=\"FOURmidables\",\"secondhome\"\r\n");
  ESP8266.setTimeout(5000);
 if(ESP8266.find("WIFI CONNECTED\r\n")==1)
 {
 Serial.println("WIFI CONNECTED");
 break;
 }
 times_check++;
 if(times_check>3) 
 {
  times_check=0;
   Serial.println("Trying to Reconnect..");
  }
  }
  ESP8266.flush();
  String cmd1 = "AT+CIPSTART=\"TCP\",\"";
  cmd1 += "184.106.153.149"; // api.thingspeak.com IP address
  cmd1 += "\",80";
  ESP8266.println(cmd1);
  Serial.print("Start Commands: ");
  Serial.println(cmd1);

  if(ESP8266.find("Error"))
  {
    Serial.println("AT+CIPSTART error");
    return;
  }
  String getStr = "GET /update?api_key=";
  getStr += myAPI;
  getStr +="&field1=";
  getStr += String(sendVal1);
  getStr +="&field2=";
  getStr += String(sendVal2);
  getStr += "\r\n\r\n";
  String cmd = "AT+CIPSEND=";
  cmd += String(getStr.length());
  ESP8266.println(cmd);
  Serial.println(cmd);

  if(ESP8266.find(">"))
  {
    ESP8266.print(getStr);
    Serial.println(getStr);
    delay(500);
    String messageBody = "";
    while (ESP8266.available()) 
    {
      String line = ESP8266.readStringUntil('\n');
      if (line.length() == 1) 
      { 
        messageBody = ESP8266.readStringUntil('\n');
      }
    }
    Serial.print("MessageBody received: ");
    Serial.println(messageBody);
    return messageBody;
  }
  else
  {
    ESP8266.println("AT+CIPCLOSE");     
    Serial.println("AT+CIPCLOSE"); 
  } 
}
