#include <LiquidCrystal.h>

LiquidCrystal lcd(12, NULL, 11, 9,8,7,6);

const int voltmetrupin = 0;
volatile int val=0; // valoare achizitionata
volatile float vout = 0.0; // tensiunea citita vout = (val * 5.0) / 1024.0;
const float R1 = 220.0; // valori rezistente divizor tensiune   
const float R2 = 220.0;
volatile float vin = 0.0; // tensiune baterie vin = vout / (R2/(R1+R2))
volatile float initialvin = 0.0; // valoarea maxima a tensiunii bateriei
volatile float i = 0.0; //intesitate curent in mA i = (vin * 1000) / (R1+R2)
const float lb = 0.6; //procent dupa care consideram ca bateria e descarcata 60%
volatile float sumvin = 0.0; // suma tensiunilor bateriei
volatile float cap = 0.0; // capacitate consumata cap = (sumvin * 10) / (R1+R2)
volatile int sec = 0;
volatile float timp = 0; // timp in minute (sec/60)

byte lowbat[8] = { // caracter pentru baterie descarcata
  B01110,
  B11111,
  B10001,
  B10001,
  B10001,
  B10001,
  B11111,
};

void setup() {  

  TIMSK1 = (1 << TOIE1); // activare timer overflow
  TCCR1A = 0; 
  TCCR1B = 0; // timer stop
  TCNT1  = 0x0BDC; // setarea valorii initiale pentru a elimina eroarea (16bit counter register)
  TCCR1B = (1 << CS12); // timer start
  
  lcd.createChar(0, lowbat);
  
  lcd.begin(16, 2);
  lcd.noCursor();
  
}
float GetTemp(void)
{
int a = analogRead(0);
float v = a * 5 / 1024.0;
float t = (v - 0.5) / 0.01;
return t;
}
void loop() {
  // put your main code here, to run repeatedly:
  
  lcd.setCursor(4,0);
  lcd.print("T");
  lcd.setCursor(6,0);
  float t = GetTemp();
  lcd.print(t);
  

}
