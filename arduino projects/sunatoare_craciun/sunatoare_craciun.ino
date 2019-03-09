/*

  This software is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License
  Attribution-ShareAlike
  CC BY-SA

  Lucrare 9 - Elemente practice de bază în dezvoltarea sistemelor cu microprocesoare integrate utilizând Arduino Uno

  Proiect tonomat
  Bazat pe exemplul de la http://www.arduino.cc/en/Tutorial/Melody
  Codarea pieselor preluata de pe http://arduino.cc/forum/index.php/topic,1390.0.html

  http://smi.aii.pub.ro

*/

#include <util/delay.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, NULL, 11, 9, 8, 7, 6);

const int speakerPin = 4;
volatile int mod = 0; // 0 - stop, 1 - play
volatile int track = 0; // numarul piesei
volatile int n;

const int length[8] = {73, 69, 71, 29, 51, 77, 64, 63}; // numarul de note din fiecare piesa
const char * notes[8] = {"ggagsed deggsgg ggagsed deggsgg DCbCDbCbabCabagabgagsgasgsesgeseddeggsgg ", \
                         "ddaagfedcdefga ddaagfedcdefga avgavCDagfdefgfgavaagfedfedgfgavCDagfed" , \
                         "cfffgagavCavafggfcfffgagavCavafggffaCDCvagfgavCcfagfccfffgagavCavafggf " , \
                         "faagfvvagaCCbCaDCvagfeagffef ", \
                         "aavCagfgagdgavCaggfgagff vavCDDaaCagfecavCagfgagff ", \
                         "cffefaagCCCvagacffefaagCffeedcCCCfvaagCCCfvaagDDDCvavgavCffgaDDDCvavgavCffgf " , \
                         "ggdgadbabCbaggsesgabsedd DCbCbabgasedggsgagdbbabCbabCbagsgCbagg ", \
                         "egbbbaCbagabgegasedeaaeesgsedgabbbaCbag DD bb baCdagabgegasede "
                        };
const byte beats[8][77] = { { 2, 2, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 2, 2, 2, 2, 2, 2, 4, 2, 2 }, \
  { 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 1, 1, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8 } , \
  { 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 6, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 6, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 6, 2 } , \
  { 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2 }, \
  { 2, 3, 1, 2, 2, 4, 4, 3, 1, 2, 2, 8, 3, 1, 2, 2, 3, 1, 4, 2, 2, 3, 1, 6, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 4, 4, 2, 2, 3, 1, 8, 8}, \
  { 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 3, 1, 2, 2, 4, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 3, 1, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 1, 1, 3, 1, 2, 2, 4, 3, 1, 2, 2, 2, 2, 4, 2, 1, 1, 3, 1, 2, 2, 4, 8 }, \
  { 2, 4, 2, 2, 4, 4, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 3, 1, 6, 2, 4, 2, 2, 4, 4, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 3, 1, 6, 8 }, \
  { 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 4, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8 }
};
const int tempo[8] = {150, 150, 150, 150, 150, 150, 150, 150};
const char * piesa[8] = {"Ding Dong Merrily on High     ", \
                         "God Rest Ye Merry Gentlemen   ", \
                         "O Little Town of Bethlehem    ", \
                         "While Shephards Watched       ", \
                         "In The Bleak Midwinter        ", \
                         "Hark the Herald               ", \
                         "O come all Ye Faithful        ", \
                         "O Come O Come Emmanuel        "
                        };

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration) {

  const char names[] = { 'c', 'd', 'e', 'f', 's', 'g', 'a', 'v', 'b', 'C', 'D', 'E' }; // note
  const int tones[] = { 1915, 1700, 1519, 1432, 1352, 1275, 1136, 1073, 1014, 956, 852, 758 }; // frecvente

  for (int i = 0; i < 12; i++) {
    if (names[i] == note) playTone(tones[i], duration);
  }
}

void setup() {
  //pinMode(2,INPUT_PULLUP);// am activat rezistentele interne 2
  //pinMode(3,INPUT_PULLUP);// am activat rezistentele interne 3
  pinMode(speakerPin, OUTPUT);
  lcd.begin(16, 2);
  lcd.noCursor();
  //activare int0 si int1
  EIMSK |= (1 << INT0);
  EIMSK |= (1 << INT1);
  //  sei();
}

void loop()
{
  if (mod == 0)
  {
    lcd.setCursor(0, 0);
    lcd.print("Stop");
    lcd.setCursor(5, 0);
    lcd.print("Piesa ");
    lcd.print(track + 1);
    lcd.setCursor(0, 1);
    lcd.print("                ");
  }
  else
  {
    for (n = 0; n < length[track]; n++)
    {
      if (mod == 0) break;
      lcd.setCursor(0, 0);
      lcd.print("Play");
      lcd.setCursor(5, 0);
      lcd.print("Piesa ");
      lcd.print(track + 1);
      lcd.setCursor(0, 1);
      for (int j = n; j < (n + 20); j++) lcd.print(piesa[track][j % 20]);
      if (notes[track][n] == ' ') delay(beats[track][n] * tempo[track]); // pauză
      else playNote(notes[track][n], beats[track][n] * tempo[track]);
    }
    // pauza intre note
    delay(tempo[track] / 2);
  }
}

ISR(INT0_vect) {
  mod = !mod;
  _delay_ms(400);
}

ISR(INT1_vect) {
  track++;
  track = (track % 8);
  n = 0; // resetez la prima nota din melodie
  _delay_ms(400);
}
